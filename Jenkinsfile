pipeline {
  agent none
  stages {
    stage('Docker Build') {
      agent any
      steps {
        sh 'docker build -t alan1402/bigdata:0.1 .'
      }
    }
    stage('Docker push') {
      agent any
      steps {
        sh 'docker push alan1402/bigdata:0.1'
      }
    }
    stage('Deployment: test stage 1') {
      agent any
      steps {
        sh 'docker compose up --build -d'
      }
    }
    stage('Deployment: test stage 2') {
      agent any
      steps {
        sh 'python3 tests/test_api.py'
        sh 'docker stop $(docker ps -a -q)'
      }
    }
  }
}