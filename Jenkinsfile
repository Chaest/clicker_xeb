pipeline{
	agent any
	stages{
		stage('Test'){
			steps{
				print 'This is a test pipeline'
			}
		}
		stage('Build'){
			steps{
				sh 'mvn clean install'				
			}
		}
	}
}
