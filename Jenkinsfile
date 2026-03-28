pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/LOKESH-7777/lokeshFreeRepo1.git'
            }
        }

        stage('Run Program') {
            steps {
                bat 'echo Running Armstrong Program'
                bat 'dir'
                bat 'py armstrong.py'
            }
        }
    }
}