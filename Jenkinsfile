
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
                echo PATH: %PATH%
                where python
                where coverage
                
                '''
            }
        }
        stage('Run Unit Tests and Generate Coverage') {
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                echo Running tests with coverage...
                python -m coverage run --source=. test_fibonacci.py
                python -m coverage xml -o coverage.xml
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
