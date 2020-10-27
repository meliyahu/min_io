import boto3
from botocore.client import Config

# Create the resource
s3 = boto3.resource('s3',
                    endpoint_url='http://localhost:9000',
                    aws_access_key_id='AKIAIOSFODNN7EXAMPLE',
                    aws_secret_access_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
                    config=Config(signature_version='s3v4'),
                    region_name='adl')



# Get the low level client from the resource
client = s3.meta.client

# generate pre signed url for bucket and object
url_boto = client.generate_presigned_url(
    "get_object",
    Params={
        "Bucket": "ecoimages",
        "Key": "Meteorology_1.png",
    },
    ExpiresIn=300,
)
print(f"url_boto={url_boto}")