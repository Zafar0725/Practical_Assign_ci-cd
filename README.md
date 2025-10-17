
# To-Do CLI Application with CI/CD

This repository contains a Python-based command-line To-Do List Manager application. It demonstrates a complete CI/CD workflow using GitHub Actions and Jenkins, including automated testing and Docker image deployment.

---

## Project Structure
```
├── app.py                 # Main CLI application
├── requirements.txt       # Python dependencies
├── tests/                 # Unit tests
│   └── test_app.py        # Contains 5+ test cases
├── Dockerfile             # Docker image definition
├── Jenkinsfile            # Jenkins pipeline configuration
└── .github/
    └── workflows/
        └── ci.yml         # GitHub Actions CI pipeline
```

---

## How to Build and Run
### Run Locally
```bash
pip install -r requirements.txt
python app.py list
```

### Run with Docker
```bash
docker pull zafar0725/todo-cli:latest
docker run zafar0725/todo-cli list
```

---

## CI Pipeline with GitHub Actions
- Located at `.github/workflows/ci.yml`
- Triggered on every `push` and `pull_request`
- Includes:
  - Dependency installation
  - Unit testing (5+ test cases)
  - Docker image build and push

### Test Scenarios
- ✅ Success: All tests pass → pipeline proceeds
- ❌ Failure: Any test fails → pipeline stops

---

## 🐳 Docker Image
- Dockerfile builds the CLI app using Python 3.11 
- Image is published to Docker Hub: `zafar0725/todo-cli:latest`

---

## 🔧 Jenkins Pipeline
- Jenkinsfile replicates GitHub Actions pipeline
- Stages:
  - Build: Install dependencies
  - Test: Run unit tests
  - Docker Build & Push: Publish image to Docker Hub

### Jenkins Setup
1. Install Python, pip, Docker, and Git on Jenkins agent
2. Add Docker credentials in Jenkins (`docker-creds`)
3. Configure Jenkins job to pull from GitHub repo
4. Use `Pipeline from SCM` with `Jenkinsfile` in root

---

## 📌 Submission
- GitHub Repository: https://github.com/Zafar0725/Practical_Assign_ci-cd
- All requirements from the assignment are implemented and validated.
