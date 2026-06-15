import subprocess
from typing import Tuple
from langchain_core.tools import tool
from agent.config import get_project_root
from agent.tools.fs_tools import safe_path_for_project


@tool
def run_cmd(
    cmd: str, cwd: str = None, timeout: int = 30
) -> Tuple[int, str, str]:
    """Runs a shell command in the specified directory and returns the result."""
    project_root = get_project_root()
    cwd_dir = safe_path_for_project(cwd) if cwd else project_root

    res = subprocess.run(
        cmd,
        shell=True,
        cwd=str(cwd_dir),
        capture_output=True,
        text=True,
        timeout=timeout,
    )

    return res.returncode, res.stdout, res.stderr
