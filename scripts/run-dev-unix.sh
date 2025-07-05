#!/bin/bash

# Ensure script runs from project root regardless of where it's called
cd "$(dirname "$0")/.." || exit 1

if [ -f ".venv/Scripts/activate" ]; then
  source .venv/Scripts/activate
elif [ -f ".venv/bin/activate" ]; then
  source .venv/bin/activate
else
  echo "[Error] Could not find virtual environment to activate."
  exit 1
fi

echo "[Dev] Starting FastAPI backend..."
uvicorn backend.api:app --reload &

sleep 2

echo "[Dev] Launching GUI..."
python main.py
