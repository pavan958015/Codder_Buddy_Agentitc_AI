from agent.llm import llm
from agent.planner.models import Plan
from agent.planner.prompts import planner_prompt

def planner_agent(state: dict) -> dict:
    """Converts user prompt into a structured Plan."""
    user_prompt = state["user_prompt"]

    resp = llm.with_structured_output(Plan).invoke(planner_prompt(user_prompt))

    if resp is None:
        raise ValueError("Planner did not return a valid response.")

    return {"plan": resp}
