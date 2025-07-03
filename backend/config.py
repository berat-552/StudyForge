import os

ENV = os.getenv("APP_ENV", "dev")  # default to dev if not set

if ENV == "prod":
    API_BASE_URL = "https://studyforge-api.onrender.com"
else:
    API_BASE_URL = "http://localhost:8000"
