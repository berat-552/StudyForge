from PySide6.QtCore import QObject, Signal, Slot
import requests
import os
from dotenv import load_dotenv

load_dotenv()


class FlashcardWorker(QObject):
    finished = Signal(str)
    error = Signal(str)

    def __init__(self, file_path, instruction):
        super().__init__()
        self.file_path = file_path
        self.instruction = instruction

        env = os.getenv("ENVIRONMENT", "dev")
        if env == "prod":
            self.api_url = os.getenv("PROD_API_URL")
        else:
            self.api_url = os.getenv("DEV_API_URL")

    @Slot()
    def run(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            response = requests.post(
                self.api_url,
                json={"text": content, "prompt": self.instruction}
            )
            response.raise_for_status()
            result = response.json().get("result", "")
            self.finished.emit(result)
        except Exception as e:
            self.error.emit(str(e))
