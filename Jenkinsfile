pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage ("Code pull"){
            steps{
                checkout scm
            }
        }
        stage('build') {
            steps {
                sh 'python --version'
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Static code metrics') {
            steps {
                echo "PEP8 style check"
                sh  'pylint --disable=C **/*.py || true'
            }
        }
    }
}