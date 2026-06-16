from agent.config import init_project_root
from agent.llm import llm
from agent.planner.models import Plan
from agent.architect.models import TaskPlan
from agent.architect.prompts import architect_prompt

def architect_agent(state: dict) -> dict:
    """Creates TaskPlan from Plan and initializes project folder."""

    plan: Plan = state["plan"]

    resp = llm.with_structured_output(TaskPlan).invoke(
        architect_prompt(plan=plan.model_dump_json())
    )

    if resp is None:
        raise ValueError("Architect did not return a valid response.")

    resp.plan = plan

    project_dir = init_project_root(plan.name)

    print("\n" + "=" * 60)
    print(f"Creating Project : {plan.name}")
    print(f"Project Folder   : {project_dir}")
    print("=" * 60 + "\n")

    return {"task_plan": resp, "project_dir": project_dir}
