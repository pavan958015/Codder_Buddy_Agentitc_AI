from langchain_core.tools import tool
from agent.resources.templates import TEMPLATES

@tool
def get_template(template_name: str) -> str:
    """Retrieves a technology template by name to help build authentication, deployment, or testing.
    
    Available templates:
    - 'auth_fastapi': FastAPI user authentication with JWT.
    - 'auth_flask': Flask session-based user authentication blueprint.
    - 'auth_frontend': Glassmorphic Login/Signup HTML frontend.
    - 'deploy_docker': Dockerfile & docker-compose.yml configuration.
    - 'deploy_render': render.yaml blueprint deployment file.
    - 'deploy_vercel': vercel.json serverless configuration.
    - 'test_unittest': A python unittest framework template.
    """
    if template_name in TEMPLATES:
        return TEMPLATES[template_name]
    else:
        available = ", ".join(f"'{k}'" for k in TEMPLATES.keys())
        return f"ERROR: Template '{template_name}' not found. Available templates: {available}"
