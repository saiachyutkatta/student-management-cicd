
pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\saiac\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    "%PYTHON%" -m venv .venv
                    if errorlevel 1 exit /b 1
                    .venv\\Scripts\\python.exe -m pip install --upgrade pip
                    if errorlevel 1 exit /b 1
                    .venv\\Scripts\\python.exe -m pip install -r requirements.txt
                    if errorlevel 1 exit /b 1
                '''
            }
        }

        stage('Test') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest -v'
            }
        }

        stage('Run Application Check') {
            steps {
                bat '.venv\\Scripts\\python.exe -m py_compile app.py'
            }
        }

        stage('Package Release') {
            steps {
                bat '''
                    if not exist release mkdir release
                    copy /Y app.py release\\app.py
                    copy /Y requirements.txt release\\requirements.txt
                '''
                archiveArtifacts artifacts: 'release/**',
                                 fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All stages completed.'
        }
        failure {
            echo 'FAILED: Check Console Output.'
        }
    }
}
