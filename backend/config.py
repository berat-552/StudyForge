import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv("APP_ENV", "dev")  # default to dev if not set

if ENV == "prod":
    API_BASE_URL = "https://studyforge-api.onrender.com"
else:
    API_BASE_URL = "http://localhost:8000"

print(f"[Config] Running in {ENV.upper()} mode. API_BASE_URL set to {API_BASE_URL}")