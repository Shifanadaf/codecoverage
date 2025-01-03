
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
                python -m pip install coverage
                
                pip show coverage
                '''
    }
}
    stage('Run Unit Tests and Generate Coverage') {
        steps {
            bat '''
            set PATH=%PYTHON_PATH%;%PATH%
            echo Running tests with coverage...
            python -m coverage run -m unittest discover
            python -m coverage xml
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
