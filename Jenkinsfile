pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
                withEnv(['MAVEN_OPTS=-Dorg.slf4j.simpleLogger.defaultLogLevel=warn']){
                    sh 'mvn clean install'
                }
            }
        }
        stage('Deploy staging'){
            steps{
                dir('playbooks/deploy'){
                    play playbooks: 'deploy.yml',
                         inventory: 'xeb.yml',
                         options:   '-e env_type=staging'
                }
            }
        }
        stage('Validate staging'){
            options{
                retry(10)
            }
            steps{
                sh 'python validity.py'
            }
        }
        stage('Deploy production'){
            steps{
                dir('playbooks/deploy'){
                    play playbooks: 'deploy.yml',
                         inventory: 'xeb.yml',
                         options:   '-e env_type=production'
                }
            }
        }
    }
}
