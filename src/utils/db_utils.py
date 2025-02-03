import mysql.connector
from mysql.connector import Error
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.utils.security import DB_CONFIG

def connect_db():
    """Establish a connection to the database."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            print("✅ Database connected successfully!")
        return conn
    except Error as e:
        print(f"❌ Error connecting to database: {e}")
        return None

def execute_query(query, params=None):
    """Execute a SQL query (SELECT, INSERT, UPDATE, DELETE)."""
    conn = connect_db()
    if conn is None:
        return None

    try:
        cursor = conn.cursor(dictionary=True)  
        cursor.execute(query, params or ())
        if query.strip().lower().startswith("select"):
            result = cursor.fetchall()
        else:
            conn.commit()
            result = cursor.rowcount  # Number of rows affected

        cursor.close()
        conn.close()
        return result
    except Error as e:
        print(f"❌ Database query error: {e}")
        return None


