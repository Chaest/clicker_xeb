# Description

This role is used to create an environment the deployment of the application.  
It work by following these steps:
 1. Create a configuration folder with all the file used to build the docker image and container (task: *generate_conf*)
 2. Tearing down existing installation
 3. Building of the image and running the container
  
An environment consist of two containers: a back and a redis server
A back is a container with both a SSHD deamon running and a tomcat server up and running.  
A redis server is a container with redis running

# Variables

This role needs the following variables to be defined:
 * **app**: The name of the application
 * **installer_base_dir**: The base directory for the installer folder

# Templates

This role uses the following templates:
 * **docker-compose.yml**: The docker-compose yaml description for the deployment of the back container
 * **Dockerfile**: The Dockerfile describing the image build for the back

# Files

This role uses the following files:
 * **wrapper.sh**: Wrapper bash script that start the SSHD daemon and the tomcat server

# Contributors

 - Emmanuel Pluot (Chaest@Github)
