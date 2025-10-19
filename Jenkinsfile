pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'zafar0725/todo-cli:latest'
    }
    stages {
        stage('Verify Tools') {
            steps {
                bat 'python --version'
                bat 'pip --version'
                bat 'git --version'
            }
        }
        stage('Build') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                bat 'python -m unittest discover -s tests -v'
            }
        }
        stage('Docker Build & Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    bat 'echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin'
                    bat "docker build -t %DOCKER_IMAGE% ."
                    bat "docker push %DOCKER_IMAGE%"
                }
            }
        }
    }
}
 