import cohere
import os
from dotenv import load_dotenv

load_dotenv()


def get_cohere_client():
    return cohere.Client(os.getenv("COHERE_API_KEY"))


def generate_study_content(text: str, prompt: str = "", co_client=None) -> str:
    co = co_client or get_cohere_client()

    base_prompt = (
        "Convert the following academic or technical text into a list of flashcard-style Q&A pairs.\n"
        "Only output the questions and answers in the exact format:\n"
        "Q: [question]\n"
        "A: [answer]\n"
        "Avoid any summaries, conclusions, instructions, or commentary.\n"
        "Do not add phrases like 'let me know if you'd like to adjust this' or anything outside the Q&A."
    )

    user_instruction = prompt.strip()
    if user_instruction:
        base_prompt += f"\n\nInstruction: {user_instruction}"

    full_prompt = f"{base_prompt}\n\nText:\n{text.strip()}"

    try:
        response = co.generate(
            model="command",
            prompt=full_prompt,
            max_tokens=600,
            temperature=0.4
        )
        return response.generations[0].text.strip()

    except Exception as e:
        return f"[Error generating study content: {str(e)}]"
