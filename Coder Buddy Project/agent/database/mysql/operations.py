import os
import pymysql
from agent.database.mysql.connection import get_mysql_connection

def initialize_mysql_db():
    """
    Initializes the MySQL database and the required tables if they do not exist.
    """
    conn = get_mysql_connection()
    if conn is None:
        print("[MySQL] Initialization skipped: Database connection unavailable.")
        return False

    db_name = os.getenv("MYSQL_DATABASE", "coder_buddy")
    try:
        with conn.cursor() as cursor:
            # Create database if not exists
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            cursor.execute(f"USE {db_name}")
            
            # Create project_runs table
            create_table_sql = """
            CREATE TABLE IF NOT EXISTS project_runs (
                id INT AUTO_INCREMENT PRIMARY KEY,
                project_name VARCHAR(255) NOT NULL,
                description TEXT,
                techstack VARCHAR(255),
                project_dir VARCHAR(512),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            """
            cursor.execute(create_table_sql)
            conn.commit()
            print(f"[MySQL] Database '{db_name}' and table 'project_runs' verified/initialized.")
            return True
    except pymysql.MySQLError as e:
        print(f"[MySQL] Error initializing database: {e}")
        return False
    finally:
        conn.close()

def save_project_run(project_name: str, description: str, techstack: str, project_dir: str) -> int:
    """
    Saves a generated project run record to the MySQL database.
    Returns the auto-generated ID of the run, or -1 if insertion fails.
    """
    # Initialize first to make sure everything exists
    initialize_mysql_db()

    conn = get_mysql_connection()
    if conn is None:
        return -1

    db_name = os.getenv("MYSQL_DATABASE", "coder_buddy")
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"USE {db_name}")
            
            insert_sql = """
            INSERT INTO project_runs (project_name, description, techstack, project_dir)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insert_sql, (project_name, description, techstack, project_dir))
            conn.commit()
            
            last_id = cursor.lastrowid
            print(f"[MySQL] Successfully saved run record. ID: {last_id}")
            return last_id
    except pymysql.MySQLError as e:
        print(f"[MySQL] Error saving run: {e}")
        return -1
    finally:
        conn.close()

def get_project_runs():
    """
    Retrieves all project run records from MySQL.
    """
    conn = get_mysql_connection()
    if conn is None:
        return []

    db_name = os.getenv("MYSQL_DATABASE", "coder_buddy")
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"USE {db_name}")
            cursor.execute("SELECT * FROM project_runs ORDER BY created_at DESC")
            return cursor.fetchall()
    except pymysql.MySQLError as e:
        print(f"[MySQL] Error retrieving runs: {e}")
        return []
    finally:
        conn.close()
