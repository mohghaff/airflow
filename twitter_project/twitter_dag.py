from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from twitter_etl import run_twitter_etl

default_args = {
    'owner': 'mohghaff',
    'retries': 2,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    dag_id='twitter_dag',
    default_args=default_args,
    description='Twitter ETL DAG',
    schedule_interval='@daily',
    start_date= datetime(2023, 1, 1)
)

run_etl = PythonOperator(
    task_id='complete_twitter_etl',
    python_callable=run_twitter_etl,
    dag=dag, 
)

run_etl