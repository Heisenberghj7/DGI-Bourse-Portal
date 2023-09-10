import os
from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


workflow = DAG(
    "Pipeline",
    schedule_interval="0 6 1 * *",
    start_date=datetime(2023, 9, 1)
)

with workflow:
    scrap = BashOperator(
        task_id='scrap_bourse',
        bash_command='pwd'
    )

    clean = BashOperator(
		task_id='clean_data',
		bash_command= 'ls'
    )

    ingest = BashOperator(
		task_id='ingest_data_database',
		bash_command= 'ls'
    )

    scrap >> clean >> ingest 

