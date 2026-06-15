import argparse
import sys
import traceback
import warnings

# Suppress deprecation and library-specific warnings for a clean CLI output
warnings.filterwarnings("ignore")

from agent.graph import agent


def main():
    parser = argparse.ArgumentParser(description="Run engineering project planner")
    parser.add_argument("--recursion-limit", "-r", type=int, default=100,
                        help="Recursion limit for processing (default: 100)")

    args = parser.parse_args()

    try:
        user_prompt = input("Enter your project prompt: ")
        result = agent.invoke(
            {"user_prompt": user_prompt},
            {"recursion_limit": args.recursion_limit}
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


if __name__ == "__main__":
    main()