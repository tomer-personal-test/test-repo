import boto3

# AWS credentials
AWS_ACCESS_KEY = 'AKIAIOSFODNN7EXAMPLE'
AWS_SECRET_KEY = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
AWS_SESSION_TOKEN = 'FwoGZXIvYXdzEBYaDJKLmnopqrsTUvwxYiK3Abc'

class AWSIntegration:
    def __init__(self):
        # Hardcoded credentials
        self.s3 = boto3.client('s3',
                              aws_access_key_id=AWS_ACCESS_KEY,
                              aws_secret_access_key=AWS_SECRET_KEY)
    
    def upload_file(self, bucket, key, filename):
        self.s3.upload_file(filename, bucket, key)
