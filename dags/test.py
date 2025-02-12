from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def my_test_function():
    print("Hello from my test DAG!")

with DAG(
    dag_id="simple_test_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    
    task = PythonOperator(
        task_id="print_message",
        python_callable=my_test_function,
    )
    
    task
