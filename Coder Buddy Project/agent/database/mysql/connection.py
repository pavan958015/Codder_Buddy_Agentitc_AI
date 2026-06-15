import os
import pymysql
from dotenv import load_dotenv

# Ensure environment variables are loaded
load_dotenv()

def get_mysql_connection():
    """
    Establishes and returns a connection to the MySQL database.
    Reads credentials and parameters from environment variables with sensible defaults.
    """
    host = os.getenv("MYSQL_HOST", "localhost")
    port_str = os.getenv("MYSQL_PORT", "3306")
    user = os.getenv("MYSQL_USER", "root")
    password = os.getenv("MYSQL_PASSWORD", "")
    database = os.getenv("MYSQL_DATABASE", "coder_buddy")

    try:
        port = int(port_str)
    except ValueError:
        port = 3306

    try:
        # Establish connection. We don't specify database yet during initialization
        # so that we can check if database exists and create it if necessary.
        conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )
        return conn
    except pymysql.MySQLError as e:
        print(f"[MySQL] Connection failed: {e}")
        return None
