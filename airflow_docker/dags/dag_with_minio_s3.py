from airflow import DAG 
from datetime import datetime, timedelta
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor


default_args= {
    'owner': 'mohghaff',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='minio_s3_v01',
    default_args=default_args,
    schedule_interval='@daily',
    start_date=datetime(2023,1,1)
) as dag:
    task_1 = S3KeySensor(
        task_id='sensor_minio_s3',
        bucket_name = 'airflow',
        bucket_key = 'data.csv',
        aws_conn_id = 'minio_conn'
    )

    task_1