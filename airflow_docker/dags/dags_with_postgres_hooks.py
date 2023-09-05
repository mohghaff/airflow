from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
import csv
import logging
from airflow.providers.amazon.aws.hooks.s3 import S3Hook


default_args = {
    'owner': 'mohghaff',
    'retries': 5,
    'retry_delay':timedelta(minutes= 5)
}


def postgres_to_s3(ds_nodash, next_ds_nodash):

    hook = PostgresHook(postgres_conn_id="postgres_localhost")
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute("select * from orders where date >= %s and date < %s", (ds_nodash, next_ds_nodash))
    with open(f"dags/get_orders_{ds_nodash}.csv", "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)
    cursor.close()
    conn.close()   
    logging.info("Saved orders file as %s", f"dags/get_orders_{ds_nodash}.csv") 

    s3_hook = S3Hook(aws_conn_id = "minio_conn")
    s3_hook.load_file(
        filename=f"dags/get_orders_{ds_nodash}.csv",
        key = f"orders/{ds_nodash}.txt",
        bucket_name = "airflow",
        replace= True
    )
 

with DAG(
    dag_id='postgres_hooks_v08',
    default_args=default_args,
    schedule_interval='@daily',
    start_date=datetime(2022,4,30)
) as dag:
    task_1 = PythonOperator(
        task_id = "postgres_to_s3",
        python_callable=postgres_to_s3
    )

    task_1