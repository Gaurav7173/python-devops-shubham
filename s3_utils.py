import boto3

s3=boto3.client('s3')

file_name="/Users/gauravkumar/Live-python-shubham/day1/api.py"

object_name="api.py"

bucket_name="devops-ai-powered-gk"

response=s3.upload_file(file_name,bucket_name,object_name)

def upload_file_to_s3(file_name, bucket_name, object_name):
    response = s3.upload_file(file_name, bucket_name, object_name)
    return response


def get_bucket():
    response = s3.list_buckets()
    return response