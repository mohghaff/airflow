from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'mohghaff',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


with DAG(
    dag_id= 'dag_with_catchup_backfill_v01',
    description='catchup and backfill',
    start_date=datetime(2023,1,1),
    schedule_interval='@daily',
    catchup=True
) as dag:
    task_1 = BashOperator(
        task_id = 'first_task',
        bash_command="echo  This is the first task."
    )

    task_1