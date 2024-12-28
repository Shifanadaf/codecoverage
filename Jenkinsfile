
pipeline {
    agent any
    environment {
        PYTHON_PATH='C:\\Python312;C:\\Python312\\Scripts'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Verify Coverage Installation') {
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                python --version
                pip install coverage
                pip show coverage
                
                '''
            }
        }
        stage('Run Unit Tests and Generate Coverage') {
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                pip install coverage
                echo "Running tests with coverage..."
                coverage run --source=. test_fibonacci.py
                coverage xml -o coverage.xml
                if exist coverage.xml (
                    echo "Coverage report generated successfully."
                ) else (
                    echo "Error: Coverage report not found!"
                    exit /b 1
                )
                '''
            }
        }
        
        stage('SonarQube Analysis') {
           environment {
                SONAR_TOKEN = credentials('sonarqube-token')
            }
            steps {
                bat '''
                    sonar-scanner -Dsonar.projectKey=democodecoverage ^
                    -Dsonar.sources=. ^
                    -Dsonar.host.url=http://localhost:9000 ^
                    -Dsonar.token=%SONAR_TOKEN% ^
                    -Dsonar.python.coverage.reportPaths=coverage.xml
                '''
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline completed successfully'
        }
        failure {
            echo 'Pipeline failed'
        }
        always {
            echo 'This runs regardless of the result.'
        }
    }
}
