import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.utils.db_utils import execute_query,fetch_query

print("🔍 Fetching employees from DB:")
employees = fetch_query("SELECT * FROM employees")
print(employees)  

print("📝 Inserting test employee:")
execute_query("INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)", ("John Doe", "Engineering", 70000))

print("🔍 Fetching employees after insert:")
employees = fetch_query("SELECT * FROM employees")
print(employees)