import os
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(env_path)

S3_BUCKET = os.getenv('S3_BUCKET')

def get_image_url(image_name):
    """
    Construye la URL pública de una imagen en S3
    """
    return f'https://{S3_BUCKET}.s3.{os.getenv("AWS_REGION", "us-east-1")}.amazonaws.com/{image_name}'