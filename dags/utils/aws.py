import boto3
from airflow.models import Variable


def aws_sesion():
    session = boto3.Session(
        aws_access_key_id=Variable.get("ACCESS_KEY"),
        aws_secret_access_key=Variable.get("SECRET_KEY"),
        region_name="eu-central-1"
    )
    return session
