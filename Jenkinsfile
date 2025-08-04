pipeline {
    agent any

    environment {
        EC2_HOST = "44.220.165.145"
        DOCKER_IMAGE = "hello-python:latest"
    }

    stages {
        stage('Checkout') {
            steps {
                echo '🔄 Checking out code from GitHub...'
                git branch: 'main', url: 'https://github.com/uppalabharadhwaj/DTCC-POC.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🐳 Building Docker image...'
                sh '''
                    set -x
                    docker build -t $DOCKER_IMAGE .
                '''
            }
        }

        stage('Save & Send Image to EC2') {
            steps {
                echo '📦 Saving Docker image and transferring to EC2...'
                withCredentials([sshUserPrivateKey(credentialsId: 'efa83a57-c6c7-4fe1-9d7b-eac6bae6f663', keyFileVariable: 'SSH_KEY')]) {
                    sh '''
                        set -x
                        docker save $DOCKER_IMAGE | bzip2 | ssh -i $SSH_KEY -o StrictHostKeyChecking=no ubuntu@$EC2_HOST "bunzip2 | docker load"
                    '''
                }
            }
        }

        stage('Run Container on EC2') {
            steps {
                echo '🚀 Running container on EC2...'
                withCredentials([sshUserPrivateKey(credentialsId: 'efa83a57-c6c7-4fe1-9d7b-eac6bae6f663', keyFileVariable: 'SSH_KEY')]) {
                    sh '''
                        set -x
                        ssh -i $SSH_KEY -o StrictHostKeyChecking=no ubuntu@$EC2_HOST << 'EOF'
                        docker stop hello-python || true
                        docker rm hello-python || true
                        docker run -d -p 5000:5000 --name hello-python hello-python:latest
EOF
                    '''
                }
            }
        }
    }

    post {
        success {
            echo '✅ Deployment successful!'
        }
        failure {
            echo '❌ Deployment failed!'
        }
    }
}