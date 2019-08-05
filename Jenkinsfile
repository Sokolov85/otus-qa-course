pipeline {
    stages {
        stage ("Code pull"){
            steps{
                checkout scm
            }
        }
        stage('Run pep8'){
            steps {
                sh 'pep8 *'
            }
        }
    }
}