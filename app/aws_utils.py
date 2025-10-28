import boto3
import os
from dotenv import load_dotenv
import sys
from flask import render_template_string

env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
if not load_dotenv(env_path):
    print(f"ERROR: No se pudo cargar el archivo .env desde {env_path}")
    sys.exit(1)

required_vars = ['AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY', 'AWS_SESSION_TOKEN', 'AWS_REGION', 'S3_BUCKET']
missing_vars = [var for var in required_vars if not os.getenv(var)]

if missing_vars:
    print(f"ERROR: Faltan las siguientes variables de entorno: {', '.join(missing_vars)}")
    sys.exit(1)

# Imprimir valores (debugging)
print("AWS Credentials loaded:")
print(f"Access Key ID: {os.getenv('AWS_ACCESS_KEY_ID')[:8]}...")
print(f"Secret Key: {os.getenv('AWS_SECRET_ACCESS_KEY')[:8]}...")
print(f"otra cosa: {os.getenv('AWS_SESSION_TOKEN')[:8]}...")
print(f"Region: {os.getenv('AWS_REGION')}")
print(f"Bucket: {os.getenv('S3_BUCKET')}")

# cliente S3
try:
    s3_client = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        aws_session_token=os.getenv('AWS_SESSION_TOKEN'),
        region_name=os.getenv('AWS_REGION')
    )
except Exception as e:
    print(f"ERROR: No se pudo crear el cliente S3: {str(e)}")
    sys.exit(1)

S3_BUCKET = os.getenv('S3_BUCKET')

def mostrar_imagenes():
    """
    Retorna una página HTML con todas las imágenes del bucket
    """
    try:
        objects = s3_client.list_objects_v2(Bucket=S3_BUCKET)
        
        image_urls = []
        
        for obj in objects.get('Contents', []):
            key = obj['Key']
            url = f'https://{S3_BUCKET}.s3.{os.getenv("AWS_REGION")}.amazonaws.com/{key}'
            image_urls.append(url)
            
        print(f"\nContenido del bucket {S3_BUCKET}:")
        for url in image_urls:
            print(f"URL generada: {url}")
            
        html = """
        <!DOCTYPE html>
        <div style="padding: 20px;">
            <h2>Imágenes en el bucket: {{ bucket_name }}</h2>
            {% for url in image_urls %}
                <div style="margin: 20px 0; padding: 10px; border: 1px solid #ccc;">
                    <img src="{{ url }}" style="max-width:300px; margin-bottom: 10px;"><br>
                    <code style="word-break: break-all;">{{ url }}</code>
                </div>
            {% endfor %}
        </div>
        """
        return render_template_string(html, image_urls=image_urls, bucket_name=S3_BUCKET)
    except Exception as e:
        print(f"Error listing bucket contents: {str(e)}")
        return f"Error: {str(e)}"

def get_image_url(image_name):
    """
    Construye la URL pública de una imagen en S3
    """
    return f'https://{S3_BUCKET}.s3.{os.getenv("AWS_REGION", "us-east-1")}.amazonaws.com/{image_name}'