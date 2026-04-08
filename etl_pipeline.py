import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Fetch the server name
server_name = os.getenv("DB_SERVER")

print("--- ETL Pipeline Initialized ---")
print(f"Target Database Server: {server_name}")
print("Secrets loaded successfully. Ready to build.")