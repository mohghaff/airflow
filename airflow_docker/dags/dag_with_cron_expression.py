from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'mohghaff',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(

    default_args= default_args,
    dag_id= 'dag_with_cron_v03',
    description= 'cron expression',
    start_date=datetime(2023, 1, 1),
    schedule_interval='0 3 * * Tue'
) as dag:

    task_1 = BashOperator(
        task_id = 'first_task',
        bash_command='echo This is the first bash.'
    )

    task_1
