pipeline {
    agent any
    stages {
        stage ("Code pull"){
            steps{
                checkout scm
            }
        }
        stage('Static code metrics') {
            steps {
                echo "PEP8 style check"
                sh  'pylint **/*.py'
            }
        }
    }
}