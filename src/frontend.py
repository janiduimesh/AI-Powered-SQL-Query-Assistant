import streamlit as st
import os
import sys
import logging
import pandas as pd
from decimal import Decimal

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# Import custom utilities
from utils.llm_utils import natural_language_to_sql
from utils.db_utils import fetch_query

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Streamlit page configuration
st.set_page_config(page_title="AI-powered SQL Query Assistant", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* General page styling */
    body {
        background-color: #f4f6f9;
        font-family: "Arial", sans-serif;
    }

    /* Title styling */
    h1 {
        color: #125D98;
        text-align: center;
        font-size: 3rem;
        margin-bottom: 20px;
    }

    /* Subtitle styling */
    .custom-text {
        font-size: 1.8rem;
        font-weight: bold;
        color: #1476D2;
        text-align: center;
        margin-bottom: 25px;
    }

    /* Input box styling */
    .stTextInput input {
        border: 2px solid #125D98;
        border-radius: 8px;
        padding: 12px;
        font-size: 1.2rem;
        width: 100%;
    }

    /* Button styling */
    .stButton button {
        background-color: #1476D2;
        color: white;
        border-radius: 8px;
        padding: 12px 25px;
        font-size: 1.2rem;
        border: none;
        font-weight: bold;
        transition: 0.3s ease-in-out;
    }

    .stButton button:hover {
        background-color: #0D5A8A;
        transform: scale(1.05);
    }

    /* Query display styling */
    .sql-query {
        background-color: #e6f2ff;
        padding: 22px;
        border-radius: 8px;
        font-family: "Courier New", monospace;
        font-weight: bold;
        font-size: 1.1rem;
        color: #2DE200;
        overflow-x: auto;
        margin-bottom: 25px;
    }

    /* Dataframe styling */
    .dataframe-container {
        border: 2px solid #1476D2;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
        padding: 15px;
        background-color: #ffffff;
        overflow-x: auto;
    }

    /* Error message styling */
    .stAlert {
        background-color: #FFCCCB;
        color: #D8000C;
        border-radius: 8px;
        padding: 12px;
        font-size: 1.2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit UI
st.title("🤖 AI-powered SQL Query Assistant")

st.markdown(
    """
    <p class="custom-text">Ask questions in plain English, and get SQL query results instantly!</p>
    """,
    unsafe_allow_html=True
)

# Input field
question = st.text_input("🔍 Ask a question (e.g., Show all employees in Engineering department):")

if question:
    st.write(f"**📝 Your question:** {question}")

    sql_query = natural_language_to_sql(question)
    
    # Display SQL query in a styled box
    st.write("**🎯 Generated SQL Query:**")
    st.markdown(f"<div class='sql-query'> {sql_query}</div>", unsafe_allow_html=True)

    try:
        results = fetch_query(sql_query)

        if results:
            # Convert Decimal values to float
            def convert_values(row):
                return {key: float(value) if isinstance(value, Decimal) else value for key, value in row.items()}
            
            flat_results = [convert_values(dict(row)) for row in results]
            df = pd.DataFrame(flat_results)

            # Display table with enhanced styling
            st.write("**✅ Query Results:**")
            st.dataframe(df)
        else:
            st.write("⚠️ No data found for the query.")
    except Exception as e:
        st.error(f"❌ **Error executing query:** {e}")
