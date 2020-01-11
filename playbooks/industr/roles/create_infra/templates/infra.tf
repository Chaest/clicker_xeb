provider "aws" {
  region     = var.region
  access_key = "{{ provider_access_key }}"
  secret_key = "{{ provider_secret_key }}"
}

resource "aws_instance" "jenkins" {
  ami                    = var.jenkins_ami
  instance_type          = var.deployment_type
  subnet_id              = aws_subnet.clicker_subnet.id
  key_name               = aws_key_pair.deploy_key.key_name
  vpc_security_group_ids = [
    aws_security_group.sec_grp.id
  ]
  tags = {
    Name = "Jenkins Instance"
  }
}

{% for env_name in environments %}
resource "aws_instance" "{{ env_name }}" {
  ami                    = var.environment_ami
  instance_type          = var.deployment_type
  subnet_id              = aws_subnet.clicker_subnet.id
  key_name               = aws_key_pair.deploy_key.key_name
  vpc_security_group_ids = [
    aws_security_group.sec_grp.id,
    aws_security_group.sec_grp_env.id
  ]
  tags = {
    Name = "The {{ env_name }} environment"
  }
}
{% endfor %}
