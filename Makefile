# Variables
APP_NAME = .

# Commands
install:
	@pip install -r requirements.txt

run:
	@uvicorn main:app --host 0.0.0.0 --port 8000 --reload

lint:
	@flake8 ${APP_NAME} --max-line-length=88
	@black --check ${APP_NAME}
	@isort --check-only ${APP_NAME}
	@mypy ${APP_NAME}

format:
	@black ${APP_NAME}
	@isort ${APP_NAME}

# Docker Commands
docker-build:
	@docker build -t ${APP_NAME} .

docker-run:
	@docker run -p 8000:8000 --env-file .env ${APP_NAME}

docker-stop:
	@docker stop $$(docker ps -q --filter ancestor=${APP_NAME})

docker-remove:
	@docker rm $$(docker ps -a -q --filter ancestor=${APP_NAME})

# Testing
test:
	@pytest

# Help
help:
	@echo "Available commands:"
	@echo "  install          Install dependencies"
	@echo "  run              Run the FastAPI app locally"
	@echo "  lint             Run lint checks"
	@echo "  format           Format code using Black and isort"
	@echo "  docker-build     Build Docker image"
	@echo "  docker-run       Run Docker container"
	@echo "  docker-stop      Stop Docker container"
	@echo "  docker-remove    Remove stopped Docker container"
	@echo "  test             Run tests"
