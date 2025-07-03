from PySide6.QtCore import QObject, Signal, Slot
import requests
from backend.config import API_BASE_URL


class FlashcardWorker(QObject):
    finished = Signal(str)
    error = Signal(str)

    def __init__(self, file_path, instruction):
        super().__init__()
        self.file_path = file_path
        self.instruction = instruction

    @Slot()
    def run(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            response = requests.post(
                f"{API_BASE_URL}/generate",
                json={"text": content, "prompt": self.instruction}
            )
            response.raise_for_status()
            result = response.json().get("result", "")
            self.finished.emit(result)
        except Exception as e:
            self.error.emit(str(e))