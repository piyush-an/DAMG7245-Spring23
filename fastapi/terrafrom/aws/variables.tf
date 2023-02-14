variable "aws_region" {
  description = "AWS region to create resources"
  type        = string
  default     = "us-east-1"
}

variable "default_tags" {
  type = object({ Course = string, Term = string, Assignment = string })
  default = {
    Course     = "damg7250"
    Term       = "spring2023"
    Assignment = "labs-demo-s3-boto"
  }
}

variable "s3_bucket_name" {
  description = "AWS S3 bucket name, Note: Bucket names can consist only of lowercase letters, numbers, dots (.), and hyphens (-)."
  type        = string
  default     = "noaa-dataset-collection-lab-demo"
}

variable "user_name" {
  description = "AWS IAM machine Username"
  type        = string
  default     = "streamlit-s3-rw"
}

variable "policy_name" {
  description = "AWS Policy Name for Read+Write Access to S3"
  type        = string
  default     = "S3-Write_Policy"
}

variable "log_group_name" {
  description = "CloudWatch logs group name"
  type        = string
  default     = "assignment01-log-group"
}

variable "log_group_retention" {
  description = "CloudWatch logs group retention days"
  type        = number
  default     = 180
}

variable "log_stream_name" {
  description = "CloudWatch stream group name"
  type        = string
  default     = "assignment01-log-stream"
}

variable "ssh_key_filename" {
  description = "the generated ssh keypair filename"
  type        = string
  default     = "ec2"
}