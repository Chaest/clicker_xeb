data "aws_vpc" "selected" {
  filter {
    name   = "tag:Name"
    values = [
      var.vpc_name
    ]
  }
}

resource "aws_subnet" "clicker_subnet" {
  vpc_id                  = data.aws_vpc.selected.id
  availability_zone       = "${var.region}a"
  cidr_block              = "{{ subnet_cidr }}"
  map_public_ip_on_launch = true
}

resource "aws_security_group" "sec_grp" {
  name   = "xeb_clicker_sec_grp"
  vpc_id = data.aws_vpc.selected.id

  ingress {
    from_port   = var.http_port
    to_port     = var.http_port
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  ingress {
    from_port   = var.ssh_port
    to_port     = var.ssh_port
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "sec_grp_env" {
  name   = "xeb_clicker_sec_grp_env"

  ingress {
    from_port   = var.deploy_port
    to_port     = var.deploy_port
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_key_pair" "deploy_key" {
  key_name   = "{{ ssh_keyname }}"
  public_key = "{{ ssh_pubkey }}"
}
