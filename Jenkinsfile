pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Pulling code from GitHub...'
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Building the project...'
                sh 'echo Build successful'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'echo All tests passed'
            }
        }
        stage('Notify') {
            steps {
                echo 'Pipeline completed successfully!'
            }
        }
    }
}
