import os
import boto3
import logging
from dotenv import load_dotenv

load_dotenv()
LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=LOGLEVEL,
    datefmt='%Y-%m-%d %H:%M:%S')

s3client = boto3.client('s3',
                        region_name='us-east-1',
                        aws_access_key_id = os.environ.get('AWS_ACCESS_KEY'),
                        aws_secret_access_key = os.environ.get('AWS_SECRET_KEY')
                        )


def list_files_in_user_bucket():
    logging.debug("fetching objects in user s3 bucket")
    my_bucket = s3client.list_objects(Bucket=os.environ.get('USER_BUCKET_NAME'))
    files = my_bucket.get('Contents')
    logging.info("Printing Files in User bucket")
    for file in files:
        print('\t' * 4 + file['Key'])

def list_files_in_noaa_bucket():
    logging.debug("fetching objects in NOAA s3 bucket")
    paginator = s3client.get_paginator('list_objects_v2')
    noaa_bucket = paginator.paginate(Bucket='noaa-goes18', PaginationConfig={"PageSize": 2})
    logging.info("Printing Files in NOAA bucket")
    for count, page in enumerate(noaa_bucket):
        files = page.get("Contents")
        for file in files:
            print('\t' * 4 + file['Key'])
        if count == 2:
            break


def main():
    # return
    list_files_in_user_bucket()
    list_files_in_noaa_bucket()


if __name__ == "__main__":
    logging.info("Script starts")
    main()
    logging.info("Script ends")