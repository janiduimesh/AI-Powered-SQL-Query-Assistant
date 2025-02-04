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
    """Executes INSERT, UPDATE, DELETE queries (non-SELECT queries)."""
    connection = connect_db() 
    if not connection:
        return
    
    try:
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()  
        print("✅ Query executed successfully!")
        return {
            "status": "success",
            "affected_rows": cursor.rowcount  
        }
    except mysql.connector.Error as err:
        print(f"❌ Database query error: {err}")
    finally:
        cursor.close()
        connection.close()

def fetch_query(query, params=None):
    """Fetch results for SELECT queries."""
    connection = connect_db()  
    if not connection:
        return None

    try:
        cursor = connection.cursor(dictionary=True)  
        cursor.execute(query, params)
        result = cursor.fetchall()
        return result  
    except mysql.connector.Error as err:
        print(f"❌ Database query error: {err}")
        return None
    finally:
        cursor.close()
        connection.close()
