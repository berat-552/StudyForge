from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.content_generator import generate_study_content

app = FastAPI()


class StudyContentRequest(BaseModel):
    text: str
    prompt: str = ""


@app.post("/generate")
def generate(request: StudyContentRequest):
    try:
        output = generate_study_content(request.text, request.prompt)
        return {"result": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
