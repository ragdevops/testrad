pipeline {
    agent {
        docker {
            filename 'Dockerfile'
            label 'zip-job-docker'
    }
    environment {
        ARTIFACTORY_URL = '''https://http://ec2-52-23-177-246.compute-1.amazonaws.com:8081/artifactory/webapp/#/home/'''
        ARTIFACTORY_USER = 'superman'
        ARTIFACTORY_PASSWORD = 'P@ssw0rd123$'
        REPO_PATH = "store-artifacts/}http://ec2-52-23-212-39.compute-1.amazonaws.com:8081/artifactory/libs-release/"
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
      stage('Publish') {
        steps {
                script {
                    def zipFiles = sh(script: 'ls }.zip', returnStdout: true).trim().split('\n')
                    zipFiles.each { zipFile ->
                        def filePath = "./${zipFile}"
                        def targetPath = "${REPO_PATH}/${zipFile}"
                        def uploadCmd = "curl -u ${ARTIFACTORY_USER}:${ARTIFACTORY_PASSWORD} -XPUT ${ARTIFACTORY_URL}/${REPO_PATH} -T ${filePath}"
                        sh uploadCmd
                    }
                    }
                }
             }
      }
       stage('Report') {
            post {
                always {
                    emailext body: "Job Status: ${currentBuild.currentResult}", subject: "Job Status Report", to: "requestor@example.com" 
                  }
              }
       }
 }
}
   
