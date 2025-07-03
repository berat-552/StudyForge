@echo off
REM Activate virtual environment
call .venv\Scripts\activate

REM Start FastAPI backend in background
start uvicorn backend.api:app --reload

REM Run frontend (this will block until user closes GUI)
python main.py
