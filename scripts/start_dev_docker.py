import subprocess
import sys
import os

CONTAINER_NAME = "studyforge-api"
IMAGE_NAME = "studyforge-api"
DOCKER_RUN_FLAGS = ["-p", "8000:8000"]
ENV_VARS = ["COHERE_API_KEY"]


def build_env_flags():
    """Convert env vars into -e KEY=VAL flags."""
    flags = []
    for key in ENV_VARS:
        val = os.getenv(key)
        if val:
            flags.extend(["-e", f"{key}={val}"])
    return flags


def start_container():
    print("[Docker] Starting container...")
    cmd = [
        "docker", "run", "-d", "--rm",
        "--name", CONTAINER_NAME,
        *DOCKER_RUN_FLAGS,
        *build_env_flags(),
        IMAGE_NAME
    ]
    subprocess.run(cmd, check=True)


def stop_container():
    print("[Docker] Stopping container...")
    try:
        subprocess.run(["docker", "stop", CONTAINER_NAME], stdout=subprocess.DEVNULL, check=True)
    except subprocess.CalledProcessError:
        print("[Warning] Failed to stop container (it may not be running).")
    except FileNotFoundError:
        print("[Error] Docker is not installed or not found in PATH.")


if __name__ == "__main__":
    start_container()
    print(f"[Docker] Container '{CONTAINER_NAME}' is running.")