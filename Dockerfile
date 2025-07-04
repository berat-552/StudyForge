FROM python:3.11-slim AS base

WORKDIR /app

ARG COHERE_API_KEY
ENV COHERE_API_KEY=${COHERE_API_KEY}

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libffi-dev \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY backend backend

EXPOSE 8000

CMD ["uvicorn", "backend.api:app", "--host", "0.0.0.0", "--port", "8000"]
