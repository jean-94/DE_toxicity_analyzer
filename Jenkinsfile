pipeline {
  agent any
  stages {
    stage('startDockerCompose build') {
      steps {
        sh 'python -m pip install --upgrade pip'
        sh 'docker-compose build'
      }
    }

    stage('DockerCompose up') {
      steps {
        sh 'docker-compose up'
      }
    }

  }
}