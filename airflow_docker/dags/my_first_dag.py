from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator


default_args = {
    'owner':'mohghaff',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)

}

with DAG(
    dag_id='myFirstDag_v5',
    default_args=default_args,
    description='This is my first DAG ever! Yay!',
    start_date=datetime(2023, 9, 2,23),
    schedule_interval='@daily'
    

) as dag:
    task_1 = BashOperator(
        task_id = 'first_task',
        bash_command =  "echo Hello world! This is my first task!"
    )
    task_2 = BashOperator(
        task_id = 'second_task',
        bash_command="echo This is the second task which will run after the first task."
    )

    task_3 = BashOperator(
        task_id = 'third_task',
        bash_command="echo This is the third task which will run simultaneoudly as task 2 after task 1."
    )
    # Task dependency method 1
    # task_1.set_downstream(task_2)
    # task_1.set_downstream(task_3)

    # Task Dependency method 2

    # task_1 >> task_2
    # task_1 >> task_3

    # Task Dependency Method 3

    task_1 >> [task_2, task_3]

