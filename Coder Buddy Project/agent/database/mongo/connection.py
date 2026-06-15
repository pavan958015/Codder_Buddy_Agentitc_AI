import os
import urllib.parse
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_mongo_client():
    """
    Establishes and returns a MongoClient connection.
    Configured with a fast timeout (2 seconds) to avoid hanging if the database is down.
    Supports either a full MONGO_URI or individual host, port, user, and password variables.
    """
    mongo_uri = os.getenv("MONGO_URI")
    
    if not mongo_uri:
        host = os.getenv("MONGO_HOST", "localhost")
        port = os.getenv("MONGO_PORT", "27017")
        user = os.getenv("MONGO_USER", "")
        password = os.getenv("MONGO_PASSWORD", "")
        
        if user and password:
            escaped_user = urllib.parse.quote_plus(user)
            escaped_password = urllib.parse.quote_plus(password)
            mongo_uri = f"mongodb://{escaped_user}:{escaped_password}@{host}:{port}/"
        else:
            mongo_uri = f"mongodb://{host}:{port}/"
    
    try:
        # We set serverSelectionTimeoutMS so we fail fast if MongoDB is not running.
        client = MongoClient(mongo_uri, serverSelectionTimeoutMS=2000)
        # Force a quick connection test
        client.admin.command('ping')
        return client
    except (ConnectionFailure, Exception) as e:
        print(f"[MongoDB] Connection failed: {e}")
        return None

def get_mongo_db():
    """
    Helper function to get the MongoDB database object directly.
    """
    client = get_mongo_client()
    if client is None:
        return None
    
    db_name = os.getenv("MONGO_DATABASE", "coder_buddy")
    return client[db_name]
