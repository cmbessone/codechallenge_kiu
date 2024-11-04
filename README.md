# KIU CodeChallenge Template

This project is a template for the KIU CodeChallenge, built with FastAPI. It provides a structured setup for quickly creating new endpoints and domains. The `Makefile` is configured to streamline development tasks, making it easy to lint, test, and format code, and prepare the app for deployment.

## Table of Contents
- [Technology](#technology)
- [Routes](#routes)
- [Pre-requisites](#pre-requisites)
- [Usage](#usage)
  - [Run App Locally](#run-app-locally)
  - [Run with Docker](#run-with-docker)
  - [Run Linter](#run-linter)
  - [Run Tests](#run-tests)
  - [Format Code](#format-code)
- [Makefile Commands](#makefile-commands)


## Technology

- **Programming Language**: Python
- **Framework**: FastAPI
- **Containerization**: Docker

## Routes

- **API Documentation (Swagger)**: [http://localhost:8000/docs](http://localhost:8000/docs)

## Pre-requisites

- **Docker** installed
- **Python 3.10+** installed
- **Linux/Mac terminal** (or emulated Linux on Windows)

## Usage

### Run App Locally

To run the application locally without Docker:

1. Install dependencies:
   ```bash
   make install

### Available Make Commands 
make "command" .  eg: make test

 ```bash
Available commands:
  install          Install dependencies
  run              Run the FastAPI app locally
  lint             Run lint checks
  format           Format code using Black and isort
  docker-build     Build Docker image
  docker-run       Run Docker container
  docker-stop      Stop Docker container
  docker-remove    Remove stopped Docker container
  test             Run tests
