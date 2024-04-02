import logging
import boto3
from botocore.exceptions import ClientError
import os
from datetime import datetime


def upload_file(fileobj, bucket = 'sethgenai', object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = 'images/' + str(datetime.now().timestamp()).replace('.','') + '.png'

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_fileobj(fileobj, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    
    # returning the generated link for s3 bucket.
    return f"https://{bucket}.s3.us-east-1.amazonaws.com/{object_name}"