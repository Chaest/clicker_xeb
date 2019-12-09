# Description

This role is used to create a Jenkins container for the deployment of the application.  
It work by following these steps:
 1. Create a configuration folder with all the file used to build the docker image and container (task: *generate_conf*)
 2. Tearing down existing installation
 3. Building of the image and running the container
 4. Performing final configuration actions to the running container (e.g. preparing a virtual environment)

# Variables

This role needs the following variables to be defined:
 * **app**: The name of the application 
 * **installer_base_dir**: The base directory for the installer folder

# Templates

This role uses the following templates:
 * **deploy_job.groovy**: The code for the pipeline job in charge of deploying the application
 * **docker-compose.yml**: The docker-compose yaml description for the deployment of the Jenkins container
 * **Dockerfile**: The Dockerfile describing the image build for Jenkins
 * **jenkins.yml**: The yaml file describing the configuration for the Jenkins image


# Files

This role uses the following files:
 * **plugins.txt**: The list of plugins to install on Jenkins
 * **reguirements.txt**: The requirements for the virtualenv installed
 * **selenium_prepare.sh**: Script used during the creation of the image to prepare the required package for selenium usage

# Requirements

The created Jenkins needs:
 * The **ldap server** to be up and running for the *authentication* to work properly
 * The **groovy library on github** to be present and functionnal for any *pipeline or other job* to work as expected
 * A **jenkins group** to exist and have at least one server, this will be the one used for this deployment 

# Contributors

 - Emmanuel Pluot (Chaest@Github)
