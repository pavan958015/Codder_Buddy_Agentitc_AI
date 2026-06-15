def route_coder(state: dict) -> str:
    """Routes after the Coder agent: to Reviewer if done, else repeat Coder."""
    if state.get("status") == "DONE":
        return "reviewer"
    return "coder"


def route_reviewer(state: dict) -> str:
    """Routes after the Reviewer agent: to END if approved, else back to Coder to fix."""
    if state.get("status") == "APPROVED":
        return "END"
    return "coder"
