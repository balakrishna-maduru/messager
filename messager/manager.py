import boto3
from botocore.exceptions import ClientError


class Manager:
    
    def __init__(self):
        pass
    
    def get_my_sender(self, secret_name = "MySender", region_name = "ap-south-1"):
        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name=region_name
        )
    
        try:
            get_secret_value_response = client.get_secret_value(
                SecretId=secret_name
            )
        except ClientError as e:
            # For a list of exceptions thrown, see
            # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
            raise e
    
        # Decrypts secret using the associated KMS key.
        return get_secret_value_response['SecretString']
        
        