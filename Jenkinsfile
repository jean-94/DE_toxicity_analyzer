pipeline {
  agent any
  stages {
    stage('startDockerCompose build') {
      steps {
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