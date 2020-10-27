import boto3

# get a boto3 client to generate STS credentials to access API
sts_client = boto3.client(
    "sts",
    region_name="qriscloud",
    use_ssl=True,
    endpoint_url="https://dl-test.tern.org.au",
)

# use current users access token to S3 credentials
# access_token = "test"
response = sts_client.assume_role_with_web_identity(
    RoleArn="arn:aws:iam::123456789012:user/svc-internal-api",
    RoleSessionName="test",
    WebIdentityToken=access_token,
    # time for session validity
    DurationSeconds=3600,
)
# using STS credentials to create an S3 client
client = boto3.client(
    "s3",
    region_name="qriscloud",
    use_ssl=True,
    endpoint_url="https://dl-test.tern.org.au",
    aws_access_key_id=response["Credentials"]["AccessKeyId"],
    aws_secret_access_key=response["Credentials"]["SecretAccessKey"],
    aws_session_token=response["Credentials"]["SessionToken"],
    config=Config(signature_version="s3v4"),
)
# generate pre signed url for bucket and object
url_boto = client.generate_presigned_url(
    "get_object",
    Params={
        "Bucket": "bioimages-test",
        "Key": "archive-sept-reindex/Shared/tern.data/bioimages-dev/wrra_bioimages/panorama/core1ha/20160916/DSC_3597.JPG",
    },
    ExpiresIn=300,
)
print(f"url_boto={url_boto}")
