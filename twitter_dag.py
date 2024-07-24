from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta,datetime
from airflow import DAG

default_args={
    'owner':'airflow',
    'depends_on_past':'False',
    'email_on_failure':'False',
    'email_on_retry':'False',
    'retries':'1',
    'retry_delay':timedelta(minutes=1),
}

dag=DAG('twitter_dag', default_args=default_args, description='my first dag',schedule_interval= timedelta(minutes=1),start_date=datetime(2023,7,21),
        catchup=False,
        )

run_etl = BashOperator(
    task_id='twitter_etl_task',
    bash_command='bash /home/anushakovi/airflow_project/wrapper_script.sh ', 
    dag=dag,
    )

run_etl