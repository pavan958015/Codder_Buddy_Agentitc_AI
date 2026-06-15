import datetime
from agent.database.mongo.connection import get_mongo_db

def save_project_details(mysql_run_id: int, plan_dict: dict, task_plan_dict: dict) -> str:
    """
    Saves the full detailed nested JSON of a project run (plan & task plan) to MongoDB.
    Links it to the structured record in MySQL using mysql_run_id.
    Returns the string ID of the inserted document, or None if insertion fails.
    """
    db = get_mongo_db()
    if db is None:
        print("[MongoDB] Operation skipped: Database connection unavailable.")
        return None

    try:
        collection = db["project_runs_details"]
        document = {
            "mysql_run_id": mysql_run_id,
            "plan": plan_dict,
            "task_plan": task_plan_dict,
            "saved_at": datetime.datetime.utcnow(),
        }
        result = collection.insert_one(document)
        inserted_id = str(result.inserted_id)
        print(f"[MongoDB] Successfully saved detailed record. Doc ID: {inserted_id}")
        return inserted_id
    except Exception as e:
        print(f"[MongoDB] Error saving detailed record: {e}")
        return None

def get_project_details(mysql_run_id: int) -> dict:
    """
    Retrieves the project run's full details document matching the mysql_run_id.
    """
    db = get_mongo_db()
    if db is None:
        return None

    try:
        collection = db["project_runs_details"]
        doc = collection.find_one({"mysql_run_id": mysql_run_id})
        if doc:
            doc["_id"] = str(doc["_id"])  # Convert ObjectId to string for easy JSON serialization
        return doc
    except Exception as e:
        print(f"[MongoDB] Error retrieving detailed record: {e}")
        return None
