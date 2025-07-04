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

dev:
	run-dev.bat

test:
	pytest

format:
	black .

# ==== Docker Workflow ====
.PHONY: docker-build docker-run docker-run-clean dev-docker docker-stop

docker-build:
	docker build -t $(IMAGE_NAME) .

docker-run:
	docker run $(DOCKER_RUN_FLAGS) $(IMAGE_NAME)

docker-run-clean:
	docker run --rm $(DOCKER_RUN_FLAGS) $(IMAGE_NAME)

dev-docker:
	@echo "Starting Docker container..."
	docker run -d --rm --name $(CONTAINER_NAME) $(DOCKER_RUN_FLAGS) $(IMAGE_NAME)
	@echo "Launching GUI..."
	python main.py
	@echo "Stopping Docker container..."
	docker stop $(CONTAINER_NAME) > /dev/null || echo "⚠️ No running container found"

docker-stop:
	-@docker stop studyforge-api && echo Stopped Docker container. || echo No running container to stop.

docker-remove:
	-@docker rm -f $(CONTAINER_NAME) && echo "Removed Docker container." || echo "No container to remove."
