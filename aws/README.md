# AWS Configuration

## Index:
This lab covers
1. [Preqrequisite](#preqrequisite)
2. [Create AWS Budget](#create-aws-budget)
3. [Create AWS S3 Bucket](#create-aws-s3-bucket)
4. [Create User for Write Access](#create-user-for-write-access)
5. [Boto3](#boto3)

## Preqrequisite 
1. Signup for AWS Free Tier Account <br>
    * https://aws.amazon.com/free/
    * https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/

Note: You are responsible for your AWS Billing.

## Tutorials

### Create AWS Budget
1. Login into AWS Console Homepage

2. Navigate to 
    > Services > AWS Cost Management > AWS Budgets

3. Click on "Create budget"

4. Choose the following options
    > Budget setup = Use a template (simplified) <br>
    > Templates - new = Zero spend budget <br>
    > Budget name = My Zero-Spend Budget <br>
    > Email recipients = "Enter email of all team members" <br>

5. Click on "Create budget"

    Refer: https://docs.aws.amazon.com/cost-management/latest/userguide/budget-templates.html

    
### Create AWS S3 Bucket
1. Login into AWS Console Homepage

2. Navigate to 
    > Services > Storage > S3

3. Click on "Create bucket"

4. Choose the following options
    > Bucket name = SomeBucketNameWhichIsUnique <br>
    > AWS Region = us-east-1 <br>
    > ACLs disabled (recommended) <br>
    > Uncheck - Block all public access <br>
    > Rest with deafult options

5. Click on "Create bucket"

6. Click on the created bucket

7. Choose 
    > Permissions > Bucket Policy Edit > Policy Generator

    Next:
    > Select Type of Policy = S3 Bucket Policy <br>
    > Effect = Allow <br>
    > Principle = * <br>
    > Actions = GetObject <br>
    > ARN = Copy from previous page and add '/*' at the end <br>

    Click Add Statement

    Generate Policy & Copy to clipboard

    Paste under Policy & Save Changes

### Create User for Write Access

1. Login into AWS Console Homepage

2. Navigate to 
    > Services > Security, Identity, & Compliance > IAM

3. Navigate to
    > Access management > Users ? Add users

4. Enter a user name
    > demowriteuseronly

5. Select 
    > Permissions options = Attach policies directly

6. Select "Create policy"

7. Choose
    > Service = S3 <br>
    > Actions > Access Level = List + Read + tagging + Write <br>
    > Resource >  <br>
        Accesspoint = any <br>
        bucket = past you bucket ARN and Any<br>
        object = past you bucket ARN and Check Object name any <br>

8. Select Next > Next

9. Enter a policyname
    > name = bucketwritepolicy

10. Create Policy

11. After you return to orginal window check the policy created "bucketwritepolicy"

12. Click Next and Create User

13. Click on the created user

14. Navigate to
    > Security credentials > Access keys > Create access key

15. Select "Command Line Interface (CLI)" and check the I Agree & Next

16. Create Access key and Download .csv file for reference later 


### Boto3

> [Boto3]() is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python, which allows Python developers to write software that makes use of services like Amazon S3 and Amazon EC2.

Links
* [Boto Github](https://github.com/boto/boto3)
* [Boto Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)

1. Create a virtual environment and activate it

2. Install `boto3` python package
    ```
    pip install boto3
    ```
3. Configure you AWS key from Step 16 above

    One of the way is to use [`python-dotenv`](https://pypi.org/project/python-dotenv/) package

    a. Create `.env` file along with [`main.py`](./main.py)

    b. Paste the following into the `.env` file

    ```bash
    AWS_ACCESS_KEY=your_aws_access_key
    AWS_SECRET_KEY=your_aws_secret_key
    ```

    c. Install `python-dotenv` package

    ```bash
    pip install python-dotenv
    ```
    d. DONOT commit your `.env` file to git

    e. Refer to [`main.py`](./main.py) futher
    ```python
    import os
    from dotenv import load_dotenv
    load_dotenv()
    ```

    f. Access your env variables
    ```python
    os.environ.get('AWS_ACCESS_KEY')
    ```

4. Connect to boto client
    ```python
    s3client = boto3.client('s3',
                        region_name='us-east-1',
                        aws_access_key_id = os.environ.get('AWS_ACCESS_KEY'),
                        aws_secret_access_key = os.environ.get('AWS_SECRET_KEY')
                        )
    ```

5. More refer to functions within the script to access objects from buckets
    ```python
    list_files_in_user_bucket()
    list_files_in_noaa_bucket()
    ```
