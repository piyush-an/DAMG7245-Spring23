
## Terraform

* Ubuntu ec2 instance
* Assign elastic ip (static)
* Creates security grup with public access to instance
* Add a ssh key pair


### Connect to EC2 instance via SSH

1. Generate ssh a key pair
    ```bash
    ssh-keygen -t rsa -b 2048 -f ec2
    ```

    > Never share your private key file and verify the file permission
    ```
    -rw-r--r-- 1 anku anku  393 Feb 14 02:09 ec2.pub
    -rw------- 1 anku anku 1811 Feb 14 02:09 ec2
    ```

2. ssh into the instance
    ```bash
    ssh -i ec2 ubuntu@<ec2-instance-ip>
    # enter yes in the prompt
    ```

3. Debug UserData errors if any 
    ```
    cat /var/log/cloud-init-output.log

    # Log too big
    cat /var/log/cloud-init.log 
    ```


