from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QLineEdit,
    QPushButton,
    QApplication,
)
from PySide6.QtCore import QThread, Slot
import sys
import os

from worker import FlashcardWorker


class AIStudyContentGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StudyForge – AI Study Assistant")
        self.setFixedSize(700, 600)
        self.setAcceptDrops(True)

        self.file_path = None
        self.thread = None
        self.worker = None

        layout = QVBoxLayout()

        self.status_label = QLabel("Drag and drop a .txt file anywhere in this window")
        layout.addWidget(self.status_label)

        self.result_box = QTextEdit()
        self.result_box.setReadOnly(True)
        self.result_box.setPlaceholderText("Generated flashcards will appear here")
        layout.addWidget(self.result_box)

        self.instruction_input = QLineEdit()
        self.instruction_input.setPlaceholderText(
            "Optional: Add extra instruction (e.g. 'Use simple terms')"
        )
        layout.addWidget(self.instruction_input)

        self.generate_button = QPushButton("Generate Flashcards")
        layout.addWidget(self.generate_button)

        self.setLayout(layout)

        self.generate_button.clicked.connect(self.handle_generate_click)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if urls and urls[0].toLocalFile().endswith(".txt"):
                event.acceptProposedAction()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            file_path = urls[0].toLocalFile()
            if file_path.endswith(".txt"):
                self.file_path = file_path
                self.status_label.setText(
                    f"✔ [{os.path.basename(file_path)}] uploaded successfully"
                )
            else:
                self.status_label.setText("❌ Only .txt files are supported.")

    def handle_generate_click(self):
        if not self.file_path:
            self.result_box.setPlainText("❌ No file selected.")
            return

        instruction = self.instruction_input.text()
        self.result_box.setPlainText("🧠 Generating content... please wait")
        self.generate_button.setEnabled(False)

        # Clean up previous thread if any
        if self.thread:
            self.thread.quit()
            self.thread.wait()

        self.thread = QThread()
        self.worker = FlashcardWorker(self.file_path, instruction)
        self.worker.moveToThread(self.thread)

        # Connect safely to slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.display_result)
        self.worker.error.connect(self.display_error)
        self.worker.finished.connect(self.cleanup_thread)
        self.worker.error.connect(self.cleanup_thread)

        self.thread.start()

    @Slot(str)
    def display_result(self, text):
        self.result_box.setPlainText(text)

    @Slot(str)
    def display_error(self, error):
        self.result_box.setPlainText(f"❌ Error generating content:\n{error}")

    @Slot()
    def cleanup_thread(self):
        self.thread.quit()
        self.thread.wait()
        self.thread = None
        self.worker = None
        self.generate_button.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AIStudyContentGenerator()
    window.show()
    sys.exit(app.exec())
