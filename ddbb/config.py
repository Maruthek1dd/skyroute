import os
from dotenv import load_dotenv

load_dotenv(override=True) 

DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME'),
    'port': int(os.getenv('DB_PORT', 3306))
    
}

print("🔧 DB_CONFIG:", DB_CONFIG) 
