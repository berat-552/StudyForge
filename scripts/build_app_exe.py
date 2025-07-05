import os
from PyInstaller.__main__ import run


def build_app_exe():
    os.environ["APP_ENV"] = "prod"
    run([
        "--onefile",
        "--windowed",
        "--name", "StudyForge",
        "main.py"
    ])


if __name__ == "__main__":
    print("[Build] Packaging StudyForge as a Windows executable...")
    build_app_exe()
    print("[Build] Done. Check the dist/ folder.")