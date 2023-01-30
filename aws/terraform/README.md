# Terraform

> [Terraform](https://www.terraform.io/) is an infrastructure as code tool that lets you build, change, and version cloud and on-prem resources safely and efficiently.

## Configure AWS Credential

* [AWS Account and Access Keys](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-appendix-sign-up.html)

* [Environment variables to configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html)

* [Configuration and credential file settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)

## Terraform Usage

1. Configure the [variables.tf](variables.tf)

2. Command: `init`

    The `terraform init` command initializes a working directory containing Terraform configuration files.
    ```bash
    terraform init
    ```

3. Command: `plan`
    
    The `terraform plan` command creates an execution plan, which lets you preview the changes that Terraform plans to make to your infrastructure. 
    ```bash
    terraform plan
    ```

4. Command: `apply`

    The `terraform apply` command executes the actions proposed in a Terraform plan.
    ```bash`
    terraform apply
    ```

5. Command: `destroy`

    The `terraform destroy` command is a convenient way to destroy all remote objects managed by a particular Terraform configuration.
    ```bash
    terraform destroy
    ```

