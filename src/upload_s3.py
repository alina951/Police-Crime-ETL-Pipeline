import boto3
from botocore.exceptions import ClientError


def upload_to_s3():

    bucket_name = "se-data-with-ai-etl-project"

    local_file = "exports/police_crimes.json"

    s3_key = "alina/police_crimes.json"

    s3 = boto3.client("s3")

    try:
        s3.upload_file(local_file, bucket_name, s3_key)
        print("JSON uploaded successfully!")

    except ClientError as e:
        print("Upload failed")
        print(e)