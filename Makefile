# ==== Config ====
IMAGE_NAME=studyforge-api
CONTAINER_NAME=studyforge-api
DOCKER_RUN_FLAGS=-p 8000:8000 -e COHERE_API_KEY=$(COHERE_API_KEY)

# ==== Dev Commands ====
.PHONY: run-backend run-gui dev test format

run-backend:
	uvicorn backend.api:app --reload

run-gui:
	python main.py

dev-windows:
	cmd /C scripts\run-dev-windows.bat

dev-unix:
	bash ./scripts/run-dev-unix.sh

test:
	pytest

format:
	black .

lint:
	flake8 .

# ==== Docker Workflow ====
.PHONY: docker-build docker-run docker-run-clean dev-docker docker-stop

docker-build:
	docker build -t $(IMAGE_NAME) .

docker-run:
	docker run $(DOCKER_RUN_FLAGS) $(IMAGE_NAME)

docker-run-clean:
	docker run --rm $(DOCKER_RUN_FLAGS) $(IMAGE_NAME)

dev-docker:
	python scripts/start_api_docker.py

docker-stop:
	-@docker stop studyforge-api && echo Stopped Docker container. || echo No running container to stop.

docker-remove:
	-@docker rm -f $(CONTAINER_NAME) && echo "Removed Docker container." || echo "No container to remove."

# ==== Docker Compose Workflow ====
.PHONY: compose-dev compose-down dev-full dev-full-down

compose-dev:
	docker compose -f docker-compose.dev.yml up

compose-down:
	docker compose -f docker-compose.dev.yml down

dev-full:
	python scripts/start_dev_full.py

dev-full-down:
	@echo "Stopping backend (Docker Compose)..."
	docker compose -f docker-compose.dev.yml down

# ==== Packaging ====
.PHONY: build clean

build:
	python scripts/build_app_exe.py

clean:
	python scripts/clean_build_artifacts.py