import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.utils.db_utils import execute_query,fetch_query

# Fetch Employees
print("🔍 Fetching employees from DB:")
employees = fetch_query("SELECT * FROM employees")
print(employees)  # Now correctly handles SELECT queries

# Insert Test Employee
print("📝 Inserting test employee:")
execute_query("INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)", ("John Doe", "Engineering", 70000))

# Fetch Again After Insert
print("🔍 Fetching employees after insert:")
employees = fetch_query("SELECT * FROM employees")
print(employees)