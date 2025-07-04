import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.content_generator import generate_study_content

app = FastAPI()


class StudyContentRequest(BaseModel):
    text: str
    prompt: str = ""


logging.basicConfig(level=logging.INFO)


@app.get("/")
def log():
    logging.info("Health check hit.")
    return {"message": "Server is running", "status": 200}


@app.post("/generate")
def generate(request: StudyContentRequest):
    try:
        output = generate_study_content(request.text, request.prompt)
        return {"result": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
