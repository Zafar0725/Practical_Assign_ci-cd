# To-Do List Manager CLI

## Description
A simple Python CLI app to manage tasks stored in a JSON file.

## Features
- Add tasks
- List tasks
- Delete tasks

## How to Run
```bash
python app.py add "Buy groceries"
python app.py add "Buy"
python app.py list
python app.py delete 1
```

## CI Pipeline
- GitHub Actions: `.github/workflows/ci.yml`
- Jenkins: `Jenkinsfile`

## Docker
```bash
docker build -t todo-cli .
docker run todo-cli
```

## Submission
- GitHub Repo: [Your Repo Link]
- Docker Image: `docker.io/yourusername/todo-cli:latest`


