import boto3
from botocore.exceptions import NoCredentialsError

s3_client = boto3.client('s3')

def upload_to_s3(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name

    try:
        s3_client.upload_file(file_name, bucket, object_name)
        return f"https://{bucket}.s3.amazonaws.com/{object_name}"
    except NoCredentialsError:
        print("Credentials not available")
        return None

