pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "mostafaelniny/flask-app"
        DOCKER_TAG = "${BUILD_NUMBER}"
    }

    options {
              skipDefaultCheckout(true) 
            }    

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Mostafaelniny/flask-app-ci-cd-pipeline.git',
                credentialsId: 'github-creds'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }

        stage('Run Container Test') {
            steps {
                sh """
                docker run -d -p 5000:5000 --name flask-test ${DOCKER_IMAGE}:${DOCKER_TAG}
                sleep 5
                docker container ls
                docker stop flask-test
                docker rm flask-test
                """
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('', 'dockerhub') {
                        docker.image("${DOCKER_IMAGE}:${DOCKER_TAG}").push()
                    }
                }
            }
        }



    }

       post {
             success {
                echo "Docker image pushed successfully!"
             }
             failure {
                echo "CI/CD pipeline failed."
             }
             always {
                sh "docker system prune -f"
            }
        }
}


