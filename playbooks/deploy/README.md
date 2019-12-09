# Description

Playbook used to deploy a build application to the tomcat server.  
It needs to be provided with an `env_type` value.

# Use

Since it is solely designed to be used during the deployment of the application on Jenkins, it should be called using the `play` DSL:
```groovy
play playbooks: deploy.yml
     inventory: xeb.yml
     options: '-e env_type=<env_type>'
```

Where env type should be the type of environment (e.g. staging).

# Contributors

 - Emmanuel Pluot (Chaest@Github)
