pipelineJob('{{ deploy_job_name }}'){
    description '''{{ deploy_job_desc }}'''
    triggers {
        githubPush()
    }
    properties{
        githubProjectUrl '{{ clicker_github_repo }}'
    }
    definition {
        cpsScm {
            scriptPath 'Jenkinsfile'
            scm {
                git {
                    remote {
                        url '{{ clicker_github_repo }}'
                        credentials 'github'
                    }
                    branch "*/master"
                }
            }
        }
    }
}
