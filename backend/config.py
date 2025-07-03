import os
from dotenv import load_dotenv

load_dotenv()  # ✅ Load the .env before reading variables

ENV = os.getenv("APP_ENV", "dev")

if ENV == "prod":
    API_BASE_URL = "https://studyforge-api.onrender.com"
else:
    API_BASE_URL = "http://localhost:8000"
