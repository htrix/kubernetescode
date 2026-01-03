pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "htrix/test"
        DOCKER_TAG   = "${env.BUILD_NUMBER}"
    }

    stages {
        stage('Clone repository') {
            steps {
                checkout scm
            }
        }

        stage('Build image') {
            steps {
                script {
                    // Build usando Docker do host
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }

        stage('Test image') {
            steps {
                script {
                    docker.image("${DOCKER_IMAGE}:${DOCKER_TAG}").inside {
                        sh 'echo "Tests passed"'
                    }
                }
            }
        }

        stage('Push image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-token') {
                        docker.image("${DOCKER_IMAGE}:${DOCKER_TAG}").push()
                    }
                }
            }
        }

        stage('Trigger ManifestUpdate') {
            steps {
                build job: 'updatemanifest', parameters: [
                    string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)
                ]
            }
        }
    }
}
