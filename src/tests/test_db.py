import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.utils.db_utils import execute_query

# Test SELECT query
print("🔍 Fetching users from DB:")
print(execute_query("SELECT * FROM employees"))

# Test INSERT query
print("📝 Inserting test employee:")
execute_query("INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)", 
              ("John Doe", "Engineering", 75000))

# Test SELECT after insert
print("🔍 Fetching users after insert:")
print(execute_query("SELECT * FROM employees"))
