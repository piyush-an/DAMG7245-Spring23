terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.52.0"
    }
  }
}

provider "aws" {
  shared_credentials_files = ["~/.aws/credentials"]
  region                   = var.aws_region

  default_tags {
    tags = var.default_tags
  }
}

resource "aws_s3_bucket" "s3_bucket" {
  bucket        = var.s3_bucket_name
  force_destroy = false
}

resource "aws_s3_bucket_public_access_block" "s3_bucket_public" {
  bucket = aws_s3_bucket.s3_bucket.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

resource "aws_s3_bucket_policy" "public_read_access" {
  bucket = aws_s3_bucket.s3_bucket.id
  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Effect" : "Allow",
        "Principal" : "*",
        "Action" : ["s3:GetObject"],
        "Resource" : [
          "${aws_s3_bucket.s3_bucket.arn}/*"
        ]
      }
    ]
  })
}

resource "aws_iam_user" "user" {
  name          = var.user_name
  force_destroy = true
}

resource "aws_iam_policy" "s3_policy" {
  name = var.policy_name
  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [

      {
        "Sid" : "ListObjectsInBucket",
        "Effect" : "Allow",
        "Action" : ["s3:ListBucket"],
        "Resource" : ["${aws_s3_bucket.s3_bucket.arn}", "*"]
      },
      {
        "Sid" : "AllObjectActions",
        "Effect" : "Allow",
        "Action" : "s3:*Object",
        "Resource" : ["${aws_s3_bucket.s3_bucket.arn}/*"]
      }
    ]
  })
}

resource "aws_iam_user_policy_attachment" "s3-policy-user" {
  user       = aws_iam_user.user.name
  policy_arn = aws_iam_policy.s3_policy.arn
}
