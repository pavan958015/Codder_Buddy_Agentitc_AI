import os
from typing import Optional
from fastapi import FastAPI, Depends

# --- Configuration and Settings ---

class DatabaseSettings:
    """Configuration settings for database connections."""
    mysql_host: str = os.getenv("MYSQL_HOST", "localhost")
    mysql_user: str = os.getenv("MYSQL_USER", "root")
    mysql_password: str = os.getenv("MYSQL_PASSWORD", "password")
    mysql_db: str = os.getenv("MYSQL_DB", "mydatabase")

    mongo_uri: str = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    mongo_db_name: str = os.getenv("MONGO_DB_NAME", "app_db")

settings = DatabaseSettings()

# --- Database Management Components ---

class MySQLConnectionManager:
    """Handles connection pooling and session management for MySQL."""
    def __init__(self, host: str, user: str, password: str, db_name: str):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name
        print(f"MySQL Connection Manager initialized for DB: {db_name}")

    def get_connection(self):
        """Simulates establishing a connection pool/session."""
        # In a real application, this would use SQLAlchemy engine or mysql-connector
        print("Attempting to establish MySQL connection...")
        return f"MySQL Connection established successfully for {self.db_name}"

    def create_user_schema(self):
        """Defines the initial structure for the 'users' table."""
        print("Defining initial MySQL schema: Creating 'users' table if it doesn't exist.")
        # Example SQL command (conceptual)
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        print("Schema definition executed.")

class MongoDBConnectionManager:
    """Handles connection and session management for MongoDB."""
    def __init__(self, uri: str, db_name: str):
        self.uri = uri
        self.db_name = db_name
        print(f"MongoDB Connection Manager initialized for DB: {db_name}")

    def get_client(self):
        """Simulates establishing a MongoDB client connection."""
        # In a real application, this would use motor or pymongo
        print("Attempting to establish MongoDB client connection...")
        return f"MongoDB Client connected to database: {self.db_name}"

    def get_database(self):
        """Returns the specific database instance."""
        return self.db_name

class DatabaseManager:
    """Central class managing all database connections and operations."""
    def __init__(self):
        print("Initializing DatabaseManager...")
        self.mysql_manager = MySQLConnectionManager(
            settings.mysql_host, settings.mysql_user, settings.mysql_password, settings.mysql_db
        )
        self.mongo_manager = MongoDBConnectionManager(
            settings.mongo_uri, settings.mongo_db_name
        )

    def get_mysql_connection(self):
        return self.mysql_manager.get_connection()

    def get_mongo_client(self):
        return self.mongo_manager.get_client()

    def setup_initial_schema(self):
        """Runs necessary initial database schema setups."""
        print("\n--- Running Initial Database Setup ---")
        self.mysql_manager.create_user_schema()
        # Add MongoDB index/collection creation logic here if needed
        print("-------------------------------------\n")

    def close_connections(self):
        """Simulates closing all active connections."""
        print("Closing database connections...")
        # Actual cleanup logic would go here
        pass


# --- FastAPI Application Setup ---
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Core Backend Infrastructure",
    description="FastAPI application with integrated MySQL and MongoDB management.",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the Database Manager globally (or via dependency injection if preferred for complex scenarios)
db_manager = DatabaseManager()

@app.on_event("startup")
async def startup_event():
    """Runs setup tasks when the application starts."""
    print("Application starting up...")
    db_manager.setup_initial_schema()


# --- Health Check Endpoint ---

@app.get("/health")
def health_check():
    """Simple endpoint to check if all core services are reachable."""
    mysql_status = db_manager.get_mysql_connection()
    mongo_status = db_manager.get_mongo_client()
    return {
        "status": "OK",
        "mysql_check": mysql_status,
        "mongo_check": mongo_status
    }

# --- Example Placeholder for CRUD Endpoint (to show integration) ---

@app.post("/users/")
def create_user(username: str, email: str):
    """Placeholder endpoint demonstrating usage of the DB manager."""
    mysql_conn = db_manager.get_mysql_connection()
    mongo_client = db_manager.get_mongo_client()

    print(f"Processing user creation for {username}...")
    # Logic to save to MySQL and MongoDB would go here
    return {"message": f"User '{username}' received. Integrated DB connections are ready."}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)