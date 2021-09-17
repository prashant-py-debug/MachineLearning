from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import timedelta
from datetime import datetime

def takes_name(**context):
    print("First function execution")
    context["ti"].xcom_push(key="mykey" , value = "first fucntion says hello!")
    

def welcome(**context):
    instance = context.get("ti").xcom_pull(key="mykey")
    print(f"hello_world by {instance}")



with DAG(
    dag_id = "first_dag",
    schedule_interval = "@daily",
    default_args = {
    "owner":"airflow",
    "retries":1,
    "retries_daily" : timedelta(minutes=5),
    "start_date" : datetime(2021,1,1),
    },
    catchup = False) as f:

    takes_name= PythonOperator(
        task_id = "takes_name",
        python_callable = takes_name,
        provide_context = True,
        )

    welcome = PythonOperator(
        task_id = "welcome",
        python_callable = welcome,
        provide_context = True,
        )

    takes_name >> welcome
