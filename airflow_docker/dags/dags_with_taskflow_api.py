from airflow.decorators import task, dag
from datetime import datetime, timedelta


default_args = {
    'owner': 'mohghaff',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


@dag(
        dag_id= 'workflow_api_dag_v002',
        default_args=default_args,
        start_date=datetime.now(),
        schedule_interval='@daily'
)
def hello_world_etl():
    

    @task(multiple_outputs = True)
    def get_name():
        return {
            'fname': 'Mohsen',
            'lname': 'Ghaffari'
        }
    
    @task()
    def get_city():
        return 'Toronto'
    
    @task()
    def greet(fname, lname, city):
        return(f"Hello {fname} {lname} from {city}.")
    


    name_dict = get_name()
    city = get_city()

    greet(fname=name_dict['fname'], lname = name_dict['lname'], city=city)


greet_dag = hello_world_etl()    

    
