from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq  # Use LangChain's ChatGroq integration
from dotenv import load_dotenv
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Initialize Groq LLM using LangChain's ChatGroq
llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model_name="llama3-70b-8192")

# Function to convert natural language to SQL
def natural_language_to_sql(question):
    try:
        logger.info(f"Received question: {question}")

        # Define the prompt template
        prompt = PromptTemplate(
            input_variables=["question"],
            template="Convert the following natural language question into an SQL query: {question}"
        )

        # Create a Runnable sequence
        chain = (
            RunnablePassthrough()  # Pass the input directly
            | prompt  # Apply the prompt template
            | llm  # Pass the output to the Groq LLM
        )

        # Invoke the chain with the question
        sql_query = chain.invoke({"question": question})
        logger.info(f"Generated SQL Query: {sql_query}")
        return sql_query.content  # Extract the content from the response
    except Exception as e:
        logger.error(f"Error generating SQL query: {e}")
        return None