pipeline {
    agent any
        docker {
            dir 'path/to/Dockerfile'
            args '-u root:root --privileged'
        }
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
        stage('Publish') {
            when {
                expression { currentBuild.resultIsBetterOrEqualTo('SUCCESS') }
            }
            steps {
                script {
                    def files = sh(
                        script: 'ls *.zip',
                        returnStdout: true
                    ).trim()
                    files.split('\n').each { file ->
                        def targetPath = "${ARTIFACTORY_SERVER}/${ARTIFACTORY_REPO}/${file}"
                        sh "curl -u ${ARTIFACTORY_USER}:${ARTIFACTORY_PASSWORD} -T ${file} ${targetPath}"
                    }
                }
            }
        }
    }
}
