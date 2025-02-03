import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.utils.llm_utils import natural_language_to_sql

# Test the LLM integration
if __name__ == "__main__":
    question = "Show all employees in the Engineering department."
    sql_query = natural_language_to_sql(question)
    print(f"Generated SQL Query: {sql_query}")
