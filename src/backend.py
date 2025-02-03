# import os
# import psycopg2  # Assuming you're using PostgreSQL. Change this depending on your DB.
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# def fetch_data_from_db(query):
#     try:
#         # Connect to your database
#         conn = psycopg2.connect(
#             host=os.getenv("DB_HOST"),
#             dbname=os.getenv("DB_NAME"),
#             user=os.getenv("DB_USER"),
#             password=os.getenv("DB_PASSWORD"),
#         )
#         cursor = conn.cursor()
        
#         # Execute the query
#         cursor.execute(query)
        
#         # Fetch the results
#         results = cursor.fetchall()
        
#         # Close the connection
#         cursor.close()
#         conn.close()
        
#         return results
    
#     except Exception as e:
#         print(f"Error: {e}")
#         return None
