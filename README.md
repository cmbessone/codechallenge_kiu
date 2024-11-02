# KIU CodeChallenge Template

This project is a template for the KIU CodeChallenge, built with FastAPI. It provides a structured setup for quickly creating new endpoints and domains. The `Makefile` is configured to streamline development tasks, making it easy to lint, test, and format code, and prepare the app for deployment.

## Table of Contents
- [Technology](#technology)
- [Routes](#routes)
- [Pre-requisites](#pre-requisites)
- [Usage](#usage)
  - [Run App Locally](#run-app-locally)
  - [Run Linter](#run-linter)
  - [Run Tests](#run-tests)
  - [Format Code](#format-code)
- [Makefile Commands](#makefile-commands)
- [Decisions Taken](#decisions-taken)
- [Features](#features)
- [Things to Improve](#things-to-improve)
- [Author](#author)

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

To run the application locally with Docker:

```bash
docker build -t kiu_codechallenge .
docker run -p 8000:8000 kiu_codechallenge
