
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'simple-app'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Source code berhasil disiapkan.'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t simple-app:latest .'
            }
        }
    }
}
