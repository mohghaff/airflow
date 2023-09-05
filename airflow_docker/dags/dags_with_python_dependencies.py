from airflow import DAG 
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'mohghaff',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


def get_sklearn():
    import sklearn
    print(f"Scikit-learn version: {sklearn.__version__}")


def get_matplotlib():
    import matplotlib
    print(f"matplotlib version: {matplotlib.__version__}")    


with DAG(
    dag_id='dags_with_python_dependencies_v03',
    default_args=default_args,
    schedule_interval='@daily',
    start_date=datetime(2023,1,1)
) as dag:
    task_1 = PythonOperator(
        task_id = 'get_sklearn',
        python_callable=get_sklearn
    )
    task_2 = PythonOperator(
        task_id='get_matplotlib',
        python_callable=get_matplotlib
    )

    task_1 >> task_2