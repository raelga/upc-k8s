output "public_ip" {
  description = "Public IP address of the Codex remote instance"
  value       = aws_instance.codex_remote.public_ip
}

output "ssh_command" {
  description = "Command to SSH into the instance"
  value       = "ssh ubuntu@${aws_instance.codex_remote.public_ip}"
}

output "instance_id" {
  value = aws_instance.codex_remote.id
}
