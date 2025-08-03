pipeline {
    agent any

    environment {
        EC2_HOST = "44.220.165.145"
        DOCKER_IMAGE = "hello-python:latest"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/uppalabharadhwaj/DTCC-POC.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Save & Send Image to EC2') {
            steps {
                sh '''
                    docker save $DOCKER_IMAGE | bzip2 | ssh -o StrictHostKeyChecking=no ubuntu@$EC2_HOST "bunzip2 | docker load"
                '''
            }
        }

        stage('Run Container on EC2') {
            steps {
                sh '''
                    ssh ubuntu@$EC2_HOST <<EOF
                    docker stop hello-python || true && docker rm hello-python || true
                    docker run -d -p 5000:5000 --name hello-python hello-python:latest
                    EOF
                '''
            }
        }
    }
}