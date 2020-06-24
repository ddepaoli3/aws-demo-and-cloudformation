#!/usr/bin/env python
import boto3
import string
import random
from datetime import datetime

BUCKET_NAME="bucket-name"
KEY=''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))

def create_date_file(event=None, context=None):
    now = datetime.now()
    binary_data=str.encode(str(now))

    # Method 2: Client.put_object()
    client = boto3.client('s3')
    client.put_object(Body=binary_data, Bucket=BUCKET_NAME, Key=KEY)
    return "new data file: " + KEY

if __name__ == '__main__':
    create_date_file()