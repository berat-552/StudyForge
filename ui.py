from PySide6.QtGui import QDragEnterEvent, QDropEvent
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTextEdit, QLineEdit,
    QPushButton
)


class DroppableLabel(QLabel):
    def __init__(self, file_drop_callback):
        super().__init__("Drag and drop a .txt file here")
        self.setAcceptDrops(True)
        self.file_drop_callback = file_drop_callback

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        urls = event.mimeData().urls()
        if urls:
            file_path = urls[0].toLocalFile()
            if file_path.endswith(".txt"):
                self.setText(f"Loaded file: {file_path}")
                self.file_drop_callback(file_path)
            else:
                self.setText("Only .txt files are supported")


class AIStudyContentGenerator(QWidget):
    def __init__(self, generate_callback):
        super().__init__()
        self.setWindowTitle("StudyForge – AI Study Assistant")
        self.setFixedSize(700, 600)

        layout = QVBoxLayout()

        self.dropped_file_path = None

        def handle_file_drop(file_path):
            self.dropped_file_path = file_path

        self.drop_label = DroppableLabel(handle_file_drop)
        layout.addWidget(self.drop_label)

        self.result_box = QTextEdit()
        self.result_box.setReadOnly(True)
        self.result_box.setPlaceholderText("Generated flashcards will appear here")
        layout.addWidget(self.result_box)

        self.instruction_input = QLineEdit()
        self.instruction_input.setPlaceholderText("Optional: Add extra instruction (e.g. 'Use simple terms')")
        layout.addWidget(self.instruction_input)

        self.generate_button = QPushButton("Generate Flashcards")
        layout.addWidget(self.generate_button)

        self.setLayout(layout)

        self.generate_button.clicked.connect(lambda: generate_callback(
            self.dropped_file_path, self.instruction_input.text(), self.result_box
        ))
