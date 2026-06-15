import argparse
import sys
import os
import zipfile
import traceback
import warnings
import asyncio
import json
import io
import queue
import threading
import contextlib
from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import StreamingResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

# Suppress deprecation and library-specific warnings for a clean CLI output
warnings.filterwarnings("ignore")

from agent.graph import agent

# --- FastAPI Web App Definition ---
app = FastAPI(title="Coder Buddy Web Orchestrator")

class QueueWriter(io.TextIOBase):
    """Intercepts print calls and puts them into a thread-safe Queue."""
    def __init__(self, q: queue.Queue):
        self.q = q
    def write(self, s):
        if s:
            self.q.put(s)
        return len(s)

@app.get("/api/stream")
def api_stream(prompt: str, recursion_limit: int = 100):
    log_queue = queue.Queue()
    writer = QueueWriter(log_queue)

    def run_agent_in_thread():
        with contextlib.redirect_stdout(writer):
            try:
                # Trigger initial state
                log_queue.put(json.dumps({"type": "node_start", "data": {"node": "planner"}}) + "\n")
                
                accumulated_state = {"user_prompt": prompt}
                # Pass a fresh dictionary clone to agent.stream to prevent mutation conflicts
                for event in agent.stream({"user_prompt": prompt}, {"recursion_limit": recursion_limit}):
                    for node, output in event.items():
                        log_queue.put(json.dumps({"type": "node_end", "data": {"node": node}}) + "\n")
                        
                        # Merge output dict keys to flatten the accumulated state
                        if isinstance(output, dict):
                            accumulated_state.update(output)
                        
                        # Predict next node activation
                        if node == "planner":
                            log_queue.put(json.dumps({"type": "node_start", "data": {"node": "architect"}}) + "\n")
                        elif node == "architect":
                            log_queue.put(json.dumps({"type": "node_start", "data": {"node": "coder"}}) + "\n")
                        elif node == "coder":
                            status = output.get("status") if isinstance(output, dict) else None
                            if status == "DONE":
                                log_queue.put(json.dumps({"type": "node_start", "data": {"node": "reviewer"}}) + "\n")
                            else:
                                log_queue.put(json.dumps({"type": "node_start", "data": {"node": "coder"}}) + "\n")
                        elif node == "reviewer":
                            status = output.get("status") if isinstance(output, dict) else None
                            if status != "APPROVED":
                                log_queue.put(json.dumps({"type": "node_start", "data": {"node": "coder"}}) + "\n")

                # Attempt to save run details to MySQL and MongoDB if available
                try:
                    plan = accumulated_state.get("plan")
                    task_plan = accumulated_state.get("task_plan")
                    project_dir = accumulated_state.get("project_dir", "")
                    
                    if plan and task_plan:
                        print("\n[Database] Logging project run metadata to MySQL...")
                        from agent.database.mysql import save_project_run
                        run_id = save_project_run(
                            project_name=plan.name,
                            description=plan.description,
                            techstack=plan.techstack,
                            project_dir=str(project_dir)
                        )
                        
                        if run_id != -1:
                            print("[Database] Logging project run details to MongoDB...")
                            from agent.database.mongo import save_project_details
                            plan_dict = plan.model_dump() if hasattr(plan, "model_dump") else plan
                            task_plan_dict = task_plan.model_dump() if hasattr(task_plan, "model_dump") else task_plan
                            save_project_details(run_id, plan_dict, task_plan_dict)
                except Exception as db_err:
                    print(f"\n[Database Warning] Could not log run details: {db_err}")

                # Yield success status with finalized project data
                plan_data = accumulated_state.get("plan")
                plan_dict = plan_data.model_dump() if hasattr(plan_data, "model_dump") else plan_data
                success_event = {
                    "type": "success",
                    "data": {
                        "plan": plan_dict,
                        "project_dir": str(accumulated_state.get("project_dir", ""))
                    }
                }
                log_queue.put(json.dumps(success_event) + "\n")
                
            except Exception as e:
                log_queue.put(json.dumps({"type": "error", "data": {"message": str(e)}}) + "\n")
            finally:
                log_queue.put("DONE\n")

    # Run execution loop inside a separate worker thread to keep FastAPI responsive
    thread = threading.Thread(target=run_agent_in_thread)
    thread.start()

    async def event_generator():
        while True:
            try:
                while not log_queue.empty():
                    item = log_queue.get_nowait()
                    if item == "DONE\n":
                        yield "data: " + json.dumps({"type": "done", "data": {}}) + "\n\n"
                        return
                    
                    if item.startswith("{"):
                        yield f"data: {item.strip()}\n\n"
                    else:
                        yield f"data: {json.dumps({'type': 'log', 'data': {'message': item.strip()}})}\n\n"
            except queue.Empty:
                pass

            if not thread.is_alive() and log_queue.empty():
                break

            await asyncio.sleep(0.1)

    return StreamingResponse(event_generator(), media_type="text/event-stream")

PROJECTS_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "Projects"))

def validate_project_dir(project_dir: str) -> str:
    abs_dir = os.path.abspath(project_dir)
    if not abs_dir.startswith(PROJECTS_ROOT):
        raise HTTPException(status_code=400, detail="Invalid project directory path.")
    if not os.path.exists(abs_dir):
        raise HTTPException(status_code=404, detail="Project directory not found.")
    return abs_dir

@app.get("/api/download")
def download_project_zip(project_dir: str):
    try:
        abs_project_dir = validate_project_dir(project_dir)
        project_name = os.path.basename(abs_project_dir)
        
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
            for root, dirs, files in os.walk(abs_project_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, abs_project_dir)
                    zip_file.write(file_path, arcname=os.path.join(project_name, rel_path))
                    
        zip_buffer.seek(0)
        return Response(
            content=zip_buffer.getvalue(),
            media_type="application/zip",
            headers={
                "Content-Disposition": f"attachment; filename={project_name}.zip"
            }
        )
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create ZIP archive: {str(e)}")

# Mount web assets to host dashboard static folder
app.mount("/ui", StaticFiles(directory="agent/ui", html=True), name="ui")

@app.get("/")
def home():
    return RedirectResponse(url="/ui/")

# --- CLI Mode Execution ---
def run_cli(recursion_limit: int):
    try:
        user_prompt = input("Enter your project prompt: ")
        result = agent.invoke(
            {"user_prompt": user_prompt},
            {"recursion_limit": recursion_limit}
        )
        print("Final State:", result)

        # Attempt to save run details to MySQL and MongoDB if available
        try:
            plan = result.get("plan")
            task_plan = result.get("task_plan")
            project_dir = result.get("project_dir", "")
            
            if plan and task_plan:
                print("\n[Database] Logging project run metadata to MySQL...")
                from agent.database.mysql import save_project_run
                run_id = save_project_run(
                    project_name=plan.name,
                    description=plan.description,
                    techstack=plan.techstack,
                    project_dir=str(project_dir)
                )
                
                if run_id != -1:
                    print("[Database] Logging project run details to MongoDB...")
                    from agent.database.mongo import save_project_details
                    plan_dict = plan.model_dump() if hasattr(plan, "model_dump") else plan
                    task_plan_dict = task_plan.model_dump() if hasattr(task_plan, "model_dump") else task_plan
                    save_project_details(run_id, plan_dict, task_plan_dict)
        except Exception as db_err:
            print(f"\n[Database Warning] Could not log run details: {db_err}")

    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        traceback.print_exc()
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Run engineering project planner")
    parser.add_argument("--recursion-limit", "-r", type=int, default=100,
                        help="Recursion limit for processing (default: 100)")
    parser.add_argument("--cli", action="store_true",
                        help="Run in terminal CLI mode instead of starting the Web UI server")
    parser.add_argument("--port", type=int, default=8000,
                        help="Port to run the Web UI server on (default: 8000)")

    args = parser.parse_args()

    if args.cli:
        run_cli(args.recursion_limit)
    else:
        print("=" * 60)
        print(f"Starting Coder Buddy Web UI on http://localhost:{args.port}/")
        print(f"   (Use 'python main.py --cli' if you want terminal mode)")
        print("=" * 60)
        uvicorn.run(app, host="0.0.0.0", port=args.port)

if __name__ == "__main__":
    main()