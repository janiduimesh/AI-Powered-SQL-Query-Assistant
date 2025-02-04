from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq  
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model_name="llama3-70b-8192")

import re
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

def natural_language_to_sql(question):
    try:
        logger.info(f"Received question: {question}")

    
        prompt = PromptTemplate(
            input_variables=["question"],
            template=(
                "Convert the following natural language question into a direct SQL query, "
                "without using INFORMATION_SCHEMA or checking table structure. "
                "The SQL query must be executable as-is: {question}"
            )
        )


        chain = (
            RunnablePassthrough()  
            | prompt  
            | llm  
        )
   
        sql_query_response = chain.invoke({"question": question})
        logger.info(f"Generated SQL Query: {sql_query_response}")

        sql_query = sql_query_response.content

        # Extract any valid SQL query (SELECT, INSERT, UPDATE, DELETE, etc.)
        match = re.search(r"(SELECT .*?;|INSERT INTO .*?;|UPDATE .*?;|DELETE .*?;|ALTER TABLE .*?;)", sql_query, re.DOTALL | re.IGNORECASE)
        
        if match:
            ans = match.group(1).strip()
            logger.info(f"Final SQL Query: {ans}")
            return ans
        else:
            logger.error("No valid SQL query found in the response.")
            return None
    except Exception as e:
        logger.error(f"Error generating SQL query: {e}")
        return None