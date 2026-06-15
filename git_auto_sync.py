import subprocess
import time
import sys
from datetime import datetime

# ANSI Escape Codes for Colors and Formatting
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

def log_info(msg):
    print(f"{BLUE}[INFO]{RESET} {msg}")

def log_success(msg):
    print(f"{GREEN}[SUCCESS]{RESET} {msg}")

def log_warning(msg):
    print(f"{YELLOW}[WARNING]{RESET} {msg}")

def log_error(msg):
    print(f"{RED}[ERROR]{RESET} {msg}")

def run_git_cmd(cmd):
    """Runs a git command and returns (stdout, stderr, returncode)."""
    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True
    )
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def get_current_branch():
    stdout, _, code = run_git_cmd("git branch --show-current")
    if code == 0 and stdout:
        return stdout
    return "main"  # Fallback branch

def check_for_changes():
    """Checks if there are any unstaged, staged, or untracked changes using git status."""
    stdout, _, code = run_git_cmd("git status --porcelain")
    if code != 0:
        return None
    if not stdout:
        return []
    # Parse changed files list
    changed_files = []
    for line in stdout.split('\n'):
        if line.strip():
            # Line format: XY path or XY "path"
            parts = line.strip().split(maxsplit=1)
            if len(parts) > 1:
                changed_files.append(parts[1])
    return changed_files

def sync_to_github(branch, debounce_time=5):
    """Stages, commits, and pushes changes to GitHub."""
    log_info(f"Change detected! Waiting {debounce_time} seconds to let edits finish...")
    time.sleep(debounce_time)
    
    # Re-check if changes are still present
    changed_files = check_for_changes()
    if not changed_files:
        log_info("Changes resolved. Auto-sync skipped.")
        return
        
    print(f"\n{BOLD}{CYAN}--- Syncing Changes to GitHub ---{RESET}")
    print(f"Files to commit:")
    for f in changed_files:
        print(f"  - {f}")
        
    # Stage all changes
    _, err, code = run_git_cmd("git add -A")
    if code != 0:
        log_error(f"Failed to run 'git add': {err}")
        return
        
    # Create commit message with local timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_msg = f"Auto-sync: Updated files at {timestamp}"
    
    _, err, code = run_git_cmd(f'git commit -m "{commit_msg}"')
    if code != 0:
        log_error(f"Failed to commit changes: {err}")
        return
    log_success(f"Changes committed locally: '{commit_msg}'")
    
    # Push to GitHub
    log_info(f"Pushing to remote origin branch: {BOLD}{branch}{RESET}...")
    _, err, code = run_git_cmd(f"git push origin {branch}")
    if code == 0:
        log_success("Successfully pushed changes to GitHub! 🚀\n")
    else:
        log_error(f"Failed to push to GitHub: {err}")
        log_warning("Push failed. Will try pushing again on the next edit.\n")

def main():
    # Welcome banner
    print(f"{BOLD}{BLUE}===================================================={RESET}")
    print(f"{BOLD}{GREEN}           🚀 GIT AUTO-SYNC SCRIPT 🚀              {RESET}")
    print(f"{BOLD}{BLUE}===================================================={RESET}")
    
    # Verify we are in a Git workspace
    _, err, code = run_git_cmd("git status")
    if code != 0:
        log_error("Directory is not a Git repository or Git is not installed.")
        log_error(err)
        sys.exit(1)
        
    branch = get_current_branch()
    log_info(f"Repository Root: {BOLD}{sys.path[0]}{RESET}")
    log_info(f"Active Branch: {BOLD}{branch}{RESET}")
    log_info("Monitoring files for changes... Press Ctrl+C to stop.\n")
    
    try:
        while True:
            changed_files = check_for_changes()
            if changed_files:
                sync_to_github(branch)
            time.sleep(5)  # Poll for changes every 5 seconds
    except KeyboardInterrupt:
        print(f"\n{BOLD}{YELLOW}Git Auto-Sync terminated.{RESET}")
        sys.exit(0)

if __name__ == "__main__":
    main()
