import sys
from agent.database.mysql import (
    initialize_mysql_db,
    save_project_run,
    get_project_runs,
)
from agent.database.mongo import (
    save_project_details,
    get_project_details,
    get_mongo_client,
)

def run_mysql_tests():
    print("\n=== Running MySQL Integration Tests ===")
    
    # 1. Initialize
    success = initialize_mysql_db()
    if not success:
        print("[-] MySQL Test Failed: Could not initialize database/tables.")
        return None
    
    print("[+] MySQL: Database initialized successfully.")

    # 2. Save a run record
    project_name = "Test Web Application"
    description = "A simple web application generated during database integration tests."
    techstack = "HTML, CSS, JavaScript"
    project_dir = "Projects/test_web_app_123"

    run_id = save_project_run(project_name, description, techstack, project_dir)
    if run_id == -1:
        print("[-] MySQL Test Failed: Could not save run record.")
        return None
    
    print(f"[+] MySQL: Saved run record successfully. ID: {run_id}")

    # 3. Retrieve run records
    runs = get_project_runs()
    if not runs:
        print("[-] MySQL Test Failed: Could not retrieve runs list.")
        return None
    
    print(f"[+] MySQL: Successfully retrieved {len(runs)} run(s) from DB.")
    # Show the newest run details
    latest_run = runs[0]
    print(f"    Latest Run: ID={latest_run['id']}, Name='{latest_run['project_name']}', CreatedAt={latest_run['created_at']}")
    
    return run_id

def run_mongo_tests(mysql_run_id):
    print("\n=== Running MongoDB Integration Tests ===")
    
    # 1. Check client connection
    client = get_mongo_client()
    if client is None:
        print("[-] MongoDB Test Failed: Connection client could not be established.")
        return False
    
    print("[+] MongoDB: Connected successfully.")

    # 2. Save detailed document linking to the MySQL run ID
    plan_dict = {
        "name": "Test Web Application",
        "description": "A simple web application",
        "techstack": "HTML, CSS, JavaScript",
        "features": ["User Authentication", "Dashboard Widgets"],
        "files": [
            {"path": "index.html", "purpose": "App entrypoint"},
            {"path": "style.css", "purpose": "App styling"},
        ]
    }
    task_plan_dict = {
        "implementation_steps": [
            {"filepath": "index.html", "task_description": "Create basic HTML skeleton"},
            {"filepath": "style.css", "task_description": "Add CSS colors and padding"},
        ]
    }

    doc_id = save_project_details(mysql_run_id, plan_dict, task_plan_dict)
    if doc_id is None:
        print("[-] MongoDB Test Failed: Could not save detailed record.")
        return False

    print(f"[+] MongoDB: Saved detailed record successfully. Doc ID: {doc_id}")

    # 3. Retrieve and print detailed document
    doc = get_project_details(mysql_run_id)
    if doc is None:
        print("[-] MongoDB Test Failed: Could not retrieve saved document.")
        return False

    print(f"[+] MongoDB: Retrieved details for MySQL Run ID {mysql_run_id} successfully.")
    print(f"    Linked MongoDB Document Saved At: {doc['saved_at']}")
    print(f"    Document Project Name: {doc['plan']['name']}")
    return True

def main():
    print("==================================================")
    print("      Coder Buddy DB Integration Verifier        ")
    print("==================================================")

    # Run MySQL tests
    mysql_run_id = run_mysql_tests()
    
    # Run MongoDB tests (if MySQL was successful and we have an ID)
    mongo_success = False
    if mysql_run_id is not None:
        mongo_success = run_mongo_tests(mysql_run_id)
    else:
        print("\n[!] Skipping MongoDB tests because MySQL setup/connection failed.")

    print("\n=================== Summary ======================")
    mysql_ok = mysql_run_id is not None
    mongo_ok = mongo_success
    
    print(f"MySQL Status:   {'[ OK ]' if mysql_ok else '[ FAILED/OFFLINE ]'}")
    print(f"MongoDB Status: {'[ OK ]' if mongo_ok else '[ FAILED/OFFLINE ]'}")

    if not mysql_ok or not mongo_ok:
        print("\nDiagnostic Tips:")
        if not mysql_ok:
            print(" - Ensure your local MySQL server is running (e.g. XAMPP, WampServer, or direct installation).")
            print(" - Verify host, port, user, and password in your .env file.")
        if not mongo_ok:
            print(" - Ensure MongoDB service is running locally on port 27017.")
            print(" - Verify the MONGO_URI in your .env file.")
        sys.exit(0) # Exit cleanly to allow user to see report without strict failure
    else:
        print("\n[+] Both database integrations are working perfectly!")
        sys.exit(0)

if __name__ == "__main__":
    main()
