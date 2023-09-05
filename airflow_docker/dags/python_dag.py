from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'mohghaff',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def get_name(ti):
    ti.xcom_push(key='fname', value='Mohsen')
    ti.xcom_push(key='lname', value='Ghaffari')

def greeting(ti, city):
    fname = ti.xcom_pull(task_ids='get_name', key='fname')
    lname = ti.xcom_pull(task_ids='get_name', key='lname')
    year = ti.xcom_pull(task_ids='get_year', key='year')
    print(f'Hello World! My name is {fname} {lname}. I am from {city}, and I have {year} years of experience. ')


def get_year(ti):
    ti.xcom_push(key='year', value=3)

with DAG(
    dag_id='python_dag_v005',
    default_args=default_args,
    description='My first dag with python operator',
    start_date=datetime.now(),
    schedule_interval='@daily'

) as dag:
    
    task_2 = PythonOperator(
        task_id ='get_name',
        python_callable=get_name
    )
    task_1 = PythonOperator(
        task_id = 'greeting',
        python_callable= greeting,
        op_kwargs={
            
            'city': 'Toronto',
            #'year': 3
        }
    )

    task_3 = PythonOperator(
        task_id = 'get_year',
        python_callable=get_year
    )
 

    [task_2, task_3] >> task_1


