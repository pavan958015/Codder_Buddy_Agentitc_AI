import os
import pathlib
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Global project root path, dynamically initialized by the architect agent
PROJECT_ROOT = None


def init_project_root(project_name: str) -> str:
    """Initializes the output project root directory in workspace/Projects/."""
    global PROJECT_ROOT

    safe_name = (
        project_name.lower()
        .replace(" ", "_")
        .replace("-", "_")
    )

    folder_name = f"{safe_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    PROJECT_ROOT = pathlib.Path.cwd() / "Projects" / folder_name
    PROJECT_ROOT.mkdir(parents=True, exist_ok=True)

    print(f"\nProject Created At: {PROJECT_ROOT}\n")
    return str(PROJECT_ROOT)


def get_project_root() -> pathlib.Path:
    """Returns the initialized PROJECT_ROOT or raises ValueError if not set."""
    if PROJECT_ROOT is None:
        raise ValueError("Project root not initialized")
    return PROJECT_ROOT
