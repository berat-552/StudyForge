FROM python:3.11-alpine AS base

WORKDIR /app

RUN apk add --no-cache build-base gcc musl-dev libffi-dev

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY backend backend
COPY .env .env

EXPOSE 8000

CMD ["uvicorn", "backend.api:app", "--host", "0.0.0.0", "--port", "8000"]
