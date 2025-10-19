# 📝 To-Do CLI Application with CI/CD

This repository contains a Python-based command-line To-Do List Manager application. It demonstrates a complete CI/CD workflow using GitHub Actions and Jenkins, including automated testing and Docker image deployment.

---

## 📦 Project Structure
```
├── app.py                 # Main CLI application
├── requirements.txt       # Python dependencies
├── tests/                 # Unit tests
│   └── test_app.py        # Contains 7+ test cases
├── Dockerfile             # Docker image definition
├── Jenkinsfile            # Jenkins pipeline configuration
└── .github/
    └── workflows/
        └── ci.yml         # GitHub Actions CI pipeline
```

---

## 🚀 Features
- Add, list, and delete tasks via CLI
- Persistent task storage using JSON
- Unit tested with `unittest`
- Dockerized for portability
- CI/CD pipelines with GitHub Actions and Jenkins

---

## 🔧 Prerequisites
- Python 3.10+
- pip
- Docker (for containerization)
- Git

---

## ⚙️ Installation
```bash
# Clone the repository
git clone https://github.com/Zafar0725/Practical_Assign_ci-cd.git
cd Practical_Assign_ci-cd

# Install dependencies
pip install -r requirements.txt
```

---

## 🧪 Testing
Run all unit tests:
```bash
python -m unittest discover -s tests -v
```

Includes:
- ✅ Valid test cases (add, delete, list, save/load)
- ❌ Invalid test case to simulate failure

To simulate a failing test:
```python
def test_failure_demo(self):
    self.assertEqual(1, 2, "This test is designed to fail")
```
---

## 🐳 Docker Usage
### Build Image
```bash
docker build -t todo-cli-app .
```

### Run Container
```bash
docker run todo-cli-app list
```

### Pull from Docker Hub
```bash
docker pull zafar0725/todo-cli:latest
docker run zafar0725/todo-cli list
```

---

## 🔁 CI/CD with GitHub Actions
- Located at `.github/workflows/ci.yml`
- Triggered on `push` and `pull_request`
- Steps:
  - Install dependencies
  - Run unit tests
  - Build and push Docker image

```
Create `.github/workflows/python-app.yml`:
```yaml
name: Python application
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.8'
    - name: Install dependencies
      run: pip install -r requirements.txt
    - name: Run tests
      run: python -m unittest discover -s tests -v
```
---

## 🧩 Jenkins Pipeline
- Defined in `Jenkinsfile`
- Stages:
  - Install dependencies
  - Run tests
  - Build and push Docker image

### Jenkins Setup
1. Install Python, pip, Docker, Git on Jenkins agent
2. Add Docker credentials (`docker-creds`) in Jenkins
3. Create a Pipeline job using `Pipeline from SCM`
4. Point to `Jenkinsfile` in repo root

---

## 🛠️ Troubleshooting
- Ensure `__pycache__/` is ignored in `.gitignore`
- Use `sys.path.insert(...)` in tests to fix import errors
- Validate Docker installation and permissions

---

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request
