data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"] # Canonical

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

data "aws_vpc" "default" {
  default = true
}

resource "aws_key_pair" "codex_remote" {
  key_name   = "${var.instance_name}-key"
  public_key = file(pathexpand(var.ssh_public_key_path))
}

resource "aws_security_group" "codex_remote" {
  name        = "${var.instance_name}-sg"
  description = "Allow SSH for Codex remote coding box"
  vpc_id      = data.aws_vpc.default.id

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.ssh_allowed_cidr]
  }

  egress {
    description = "All outbound"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.instance_name}-sg"
  }
}

resource "aws_instance" "codex_remote" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = var.instance_type
  key_name               = aws_key_pair.codex_remote.key_name
  vpc_security_group_ids = [aws_security_group.codex_remote.id]

  root_block_device {
    volume_size = var.root_volume_size_gb
    volume_type = "gp3"
  }

  user_data = file("${path.module}/user_data.sh.tpl")

  tags = {
    Name = var.instance_name
  }
}
