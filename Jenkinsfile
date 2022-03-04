pipeline {
  agent any
  stages {
    stage('startDockerCompose build') {
      steps {
        sh 'pip --upgrade'
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