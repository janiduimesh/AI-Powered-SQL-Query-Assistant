# AI-Powered-SQL-Query-Assistant

An AI-based application that converts natural language queries into SQL statements and executes them on a database. The system also supports executing INSERT, UPDATE, DELETE, and complex queries with ORDER BY and HAVING clauses.

## 🚀 Features
- **Natural Language to SQL Conversion**: Generate SQL queries from user input.
- **Query Execution**: Supports SELECT, INSERT, UPDATE, DELETE queries.
- **Error Handling**: Displays errors in a user-friendly format.
- **Streamlit Frontend**: Interactive web UI for querying the database.

## 🛠️ Technologies Used
- **Python**
- **LangChain (LLM Integration)**
- **Streamlit (Frontend)**
- **SQLite / MySQL (Database)**
- **Regex (Query Parsing)**
- **Logging (Debugging and Error Handling)**

## 📂 Project Structure
```
📦 AI_SQL_Generator
 ┣ 📂 app
 ┃ ┣ 📜 main.py         # Streamlit Frontend
 ┃ ┣ 📜 llm_util.py     # AI Query Generation Logic
 ┃ ┣ 📜 db_util.py      # Database Connection & Execution
 ┣ 📜 README.md        # Project Documentation
 ┣ 📜 requirements.txt  # Dependencies
```

## 🔧 Setup Instructions
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/AI-SQL-Generator.git
   cd AI-SQL-Generator
   ```
2. **Create Virtual Environment** (Optional but recommended)
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Application**
   ```bash
   streamlit run app/main.py
   ```

## 📌 Example Queries
- **Retrieve all employees earning more than $50,000:**
  ```sql
  SELECT name, department FROM employees WHERE salary > 50000;
  ```
- **Insert a new employee:**
  ```sql
  INSERT INTO employees (name, department, salary) VALUES ('Alice', 'HR', 60000);
  ```
- **Update salary of employees in IT department:**
  ```sql
  UPDATE employees SET salary = salary + 5000 WHERE department = 'IT';
  ```
- **Delete an employee:**
  ```sql
  DELETE FROM employees WHERE name = 'John Doe';
  ```
- **List employees in descending salary order:**
  ```sql
  SELECT name, salary FROM employees ORDER BY salary DESC;
  ```
- **Get departments with average salary above $50,000:**
  ```sql
  SELECT department, AVG(salary) FROM employees GROUP BY department HAVING AVG(salary) > 50000;
  ```

## 🔗 Important Links
- **GitHub Repository**: [Your GitHub Repo](https://github.com/your-username/AI-SQL-Generator)
- **Project Demo**: [Live Streamlit App](https://your-app-url.streamlit.app)

## 🤝 Contribution
Feel free to fork this repo, create a new branch, and submit a pull request! 🙌

## 📜 License
This project is licensed under the MIT License.
