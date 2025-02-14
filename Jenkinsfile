pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-webapp"
        CONTAINER_NAME = "flask-webapp-container"
    }

    stages {
        stage('Checkout') {
            steps {
                // Replace the URL below with your GitHub repository URL
                git 'https://github.com/your-username/your-repository.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }
        stage('Run Docker Container') {
            steps {
                // Run container in detached mode mapping host port 5000 to container port 5000
                sh 'docker run -d --name $CONTAINER_NAME -p 5000:5000 $IMAGE_NAME'
            }
        }
    }
    post {
        always {
            echo 'Cleaning up Docker containers...'
            // Stop and remove the container if it exists
            sh 'docker stop $CONTAINER_NAME || true'
            sh 'docker rm $CONTAINER_NAME || true'
        }
    }
}