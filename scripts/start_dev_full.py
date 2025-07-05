import subprocess
import time
import sys
import os

DOCKER_COMPOSE_FILE = "docker-compose.dev.yml"
BACKEND_SERVICE_NAME = "studyforge-api"
GUI_ENTRY = "main.py"


def start_backend():
    print("[Start] Launching backend using Docker Compose...")
    subprocess.Popen(
        ["docker", "compose", "-f", DOCKER_COMPOSE_FILE, "up"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        shell=os.name == "nt"  # only use shell=True on Windows
    )
    time.sleep(3)  # Allow time for the container to boot


def launch_gui():
    print("[Start] Launching GUI...")
    subprocess.run([sys.executable, GUI_ENTRY])


def stop_backend():
    print("[Stop] Stopping backend...")
    subprocess.run(["docker", "compose", "-f", DOCKER_COMPOSE_FILE, "down"])


if __name__ == "__main__":
    try:
        start_backend()
        launch_gui()
    finally:
        stop_backend()
