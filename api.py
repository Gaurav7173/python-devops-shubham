from fastapi import FastAPI
from system_utils import get_system_info
import boto3

s3=boto3.resource('s3')

app = FastAPI(title="devops api")

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}


@app.get("/metrics")
def metrics():

    """
    Get system metrics including CPU, memory, and disk usage.
    Returns:
        dict: A dictionary containing CPU, memory, and disk usage percentages.
    """
    return get_system_info()

@app.get("/aws/s3")
def get_bucket():
    buckets = []
    for bucket in s3.buckets.all():
        buckets.append(bucket.name)
    return buckets


