import os
from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

default_args= {
        "depends_on_past": False,
        "email": ["medhajjari9@gmail.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        # "retry_delay": timedelta(minutes=5),
        # 'queue': 'bash_queue',
        # 'pool': 'backfill',
        # 'priority_weight': 10,
        # 'end_date': datetime(2016, 1, 1),
        # 'wait_for_downstream': False,
        # 'sla': timedelta(hours=2),
        # 'execution_timeout': timedelta(seconds=300),
        # 'on_failure_callback': some_function, # or list of functions
        # 'on_success_callback': some_other_function, # or list of functions
        # 'on_retry_callback': another_function, # or list of functions
        # 'sla_miss_callback': yet_another_function, # or list of functions
        # 'trigger_rule': 'all_success'
    }

with DAG(
    "Pipeline",
    default_args=default_args,
    description="A simple tutorial DAG",
    schedule_interval="0 6 1 * *",
    start_date=datetime(2023, 9, 1),
) as dag:
    
    scrap = BashOperator(
        task_id='scrap_bourse',
        bash_command='pwd'
    )

    clean = BashOperator(
		  task_id='clean_data',
		  bash_command= 'ls'
    )

    nlp = BashOperator(
		  task_id='NLP',
		  bash_command= 'curl'
    )

    ingest = BashOperator(
		  task_id='ingest_data_database',
		  bash_command= 'whoami'
    )

    scrap >> clean >> nlp >> ingest 

