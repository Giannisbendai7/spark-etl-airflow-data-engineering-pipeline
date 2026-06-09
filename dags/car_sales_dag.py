from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

def run_spark_job():
    subprocess.run([
        "python",
        "/opt/airflow/spark_jobs/etl_pipeline.py"
    ])

with DAG(
    dag_id="car_sales_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    task_etl = PythonOperator(
        task_id="run_spark_etl",
        python_callable=run_spark_job
    )

    task_etl
