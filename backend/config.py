import os
import sys


def is_frozen():
    return getattr(sys, 'frozen', False)


# Default to prod if frozen (i.e. built with PyInstaller)
ENV = os.getenv("APP_ENV", "dev")
if is_frozen() and ENV == "dev":
    ENV = "prod"

if ENV == "prod":
    API_BASE_URL = "https://studyforge-api.onrender.com"
else:
    API_BASE_URL = "http://localhost:8000"

print(f"[Config] Running in {ENV.upper()} mode. API_BASE_URL set to {API_BASE_URL}")
