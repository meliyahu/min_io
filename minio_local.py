import boto3
from botocore.client import Config

class MinIo():
    def __init__(self, bucket, file_name):
        self.bucket = bucket
        self.file_name = file_name
       # Create the resource
        self.s3 = boto3.resource('s3',
                    endpoint_url='http://localhost:9000',
                    aws_access_key_id='AKIAIOSFODNN7EXAMPLE',
                    aws_secret_access_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
                    config=Config(signature_version='s3v4'),
                    region_name='adl')

        # Get the low level client from the resource
        self.client = self.s3.meta.client
    def get_url(self):
        # generate pre signed url for bucket and object
        url_boto = self.client.generate_presigned_url(
            "get_object",
            Params={
            "Bucket": self.bucket,
            "Key": self.file_name,
            },
            ExpiresIn=300,
            )
        return url_boto