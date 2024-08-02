# pipeline/pipeline.py
import boto3
import pandas as pd
from sqlalchemy import create_engine
from config import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_S3_BUCKET,
    REDSHIFT_HOST,
    REDSHIFT_PORT,
    REDSHIFT_DB,
    REDSHIFT_USER,
    REDSHIFT_PASSWORD,
)

def upload_to_s3(file_name, bucket, object_name=None):
    s3_client = boto3.client('s3',
                             aws_access_key_id=AWS_ACCESS_KEY_ID,
                             aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    if object_name is None:
        object_name = file_name
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except Exception as e:
        print(f'Error uploading file to S3: {e}')
        return False
    return True

def load_csv_to_redshift(file_path, table_name, s3_bucket):
    df = pd.read_csv(file_path)
    csv_s3_path = f's3://{s3_bucket}/{file_path}'
    
    upload_to_s3(file_path, s3_bucket, file_path)
    
    redshift_conn_str = f'postgresql+psycopg2://{REDSHIFT_USER}:{REDSHIFT_PASSWORD}@{REDSHIFT_HOST}:{REDSHIFT_PORT}/{REDSHIFT_DB}'
    engine = create_engine(redshift_conn_str)

    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f'Table {table_name} loaded to Redshift successfully.')

if __name__ == '__main__':
    file_path = 'taxidata.csv'
    table_name = 'taxidata'
    load_csv_to_redshift(file_path, table_name, AWS_S3_BUCKET)
