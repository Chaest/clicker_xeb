# Description

This role is used to provision the infrastructure of the industrialization on AWS.  
It work by following these steps:
 1. It generates the terraform configuration for the infrastructure
 2. It ensures the infrastructure is provisionned
 3. It adds the following hosts: Jenkins, the "environment group" with the environments.
  
All provisionned machines are  t2.micro AWS Ubuntu.

# Variables

This role can work fine on its own.  
The `environments` variables can be changed to add or remove environments.

# Templates

This role uses the following templates:
 * **infra.tf**: The terraform file discribing the machines
 * **network.tf**: The terraform file with all network related objects
 * **output.tf**: The terraform file with all the outputs after the application of the files
 * **variables.tf**: The terraform file with all the variables used in the other files

# Contributors

 - Emmanuel Pluot (Chaest@Github)
