variable "project_id" {
  description = "Google Cloud Platform (GCP) Project ID."
  type        = string
  default     = "vertical-set-375108"
}

variable "region" {
  description = "GCP region name."
  type        = string
  default     = "us-east1"
}

variable "zone" {
  description = "GCP zone name."
  type        = string
  default     = "us-east1-b"
}

variable "name" {
  description = "Web server name."
  type        = string
  default     = "demo-labs"
}

variable "machine_type" {
  description = "GCP VM instance machine type."
  type        = string
  default     = "e2-standard-4" # e2-medium e2-standard-2 e2-standard-4
}

variable "gce_ssh_user" {
  description = "the generated ssh keypair filename"
  type        = string
  # default     = "piyush_dezc_2023"
  default = "ubuntu"
}

variable "ssh_key_filename" {
  description = "the generated ssh keypair filename"
  type        = string
  default     = "ce"
}
