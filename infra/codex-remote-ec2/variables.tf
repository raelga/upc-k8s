variable "aws_profile" {
  description = "AWS CLI profile to use"
  type        = string
  default     = "talks"
}

variable "aws_region" {
  description = "AWS region to deploy into"
  type        = string
  default     = "us-east-1"
}

variable "instance_type" {
  description = "EC2 instance type (free-tier eligible)"
  type        = string
  default     = "t2.micro"
}

variable "root_volume_size_gb" {
  description = "Root EBS volume size in GB (free tier allows up to 30GB total)"
  type        = number
  default     = 20
}

variable "ssh_public_key_path" {
  description = "Path to the local SSH public key to install on the instance"
  type        = string
  default     = "~/.ssh/id_rsa.pub"
}

variable "ssh_allowed_cidr" {
  description = "CIDR block allowed to SSH into the instance. Use 0.0.0.0/0 for roaming phone access, or restrict to a specific IP/CIDR."
  type        = string
  default     = "0.0.0.0/0"
}

variable "instance_name" {
  description = "Name tag for the EC2 instance"
  type        = string
  default     = "codex-remote"
}
