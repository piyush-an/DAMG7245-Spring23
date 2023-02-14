output "elastic_public_ip" {
  value       = aws_eip.elastic_ip.public_ip
  description = "The elastic IP "
}