variable "jenkins_ami" {
  description = "The AMI used by to create the Jenkins server"
  type        = string
  default     = "{{ amis['jenkins'] }}"
}
variable "environment_ami" {
  description = "The AMI used by the different environment instances"
  type        = string
  default     = "{{ amis['environment'] }}"
}
variable "deployment_type" {
  description = "The type of instances this deployment should use"
  type        = string
  default     = "{{ deploy_type }}"
}
variable "http_port" {
  description = "The HTTP port"
  type        = number
  default     = {{ ports['http'] }}
}
variable "ssh_port" {
  description = "The SSH port"
  type        = number
  default      = {{ ports['ssh'] }}
}
variable "deploy_port" {
  description = "The deployment port"
  type        = number
  default      = {{ ports['container_ssh'] }}
}
variable "vpc_name" {
  description = "The name of the VPC to use"
  type        = string
  default     = "{{ vpc_name }}"
}
variable "region" {
  description = "The aws region to use"
  type        = string
  default     = "{{ provider_region }}"
}
