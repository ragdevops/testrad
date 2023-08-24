pipeline {
    agent any
    environment {
        ARTIFACTORY_URL = '''https://http://ec2-52-23-177-246.compute-1.amazonaws.com:8081/artifactory/webapp/#/home/'''
        ARTIFACTORY_USER = 'superman'
        ARTIFACTORY_PASSWORD = 'P@ssw0rd123$'
        REPO_PATH = "store-artifacts/${env.VERSION}"
    }
    stages{
      stage('Checkout Source') {
         steps {
            git branch: 'main', url: 'https://github.com/ragdevops/testrad.git'             
      }
    }
        stage('Build') {
            steps {
                sh 'python3 zip_job.py'
            }
        }
    }
}
