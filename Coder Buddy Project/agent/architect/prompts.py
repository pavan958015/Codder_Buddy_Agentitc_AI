def architect_prompt(plan: str) -> str:
    ARCHITECT_PROMPT = f"""
You are the ARCHITECT agent. Given this project plan, break it down into explicit engineering tasks.

RULES:
- For each FILE in the plan, create one or more IMPLEMENTATION TASKS.
- Ensure tasks are explicitly created for:
    * User Authentication (if requested/applicable).
    * Automated tests (e.g. test_*.py unit tests).
    * Deployment configurations (e.g. Dockerfile, docker-compose.yml, render.yaml, vercel.json) and DEPLOY.md.
- In each task description:
    * Specify exactly what to implement.
    * Name the variables, functions, classes, and components to be defined.
    * Mention how this task depends on or will be used by previous tasks.
    * Include integration details: imports, expected function signatures, data flow.
- Order tasks so that dependencies (e.g., helper utilities, DB configuration, auth endpoints) are implemented first, then application logic, then unit tests, and finally deployment configurations.
- Each step must be SELF-CONTAINED but also carry FORWARD the relevant context from earlier tasks.

Project Plan:
{plan}
    """
    return ARCHITECT_PROMPT
