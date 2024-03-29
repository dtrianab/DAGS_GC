import os
import datetime
from airflow import DAG
from airflow import settings
from airflow.providers.postgres.operators.postgres import PostgresOperator


with DAG(
    # instantiating the Postgres Operator
    dag_id="postgres_init",
    start_date=datetime.datetime(2020, 2, 2),
    schedule_interval="@once",
    catchup=True,
) as dag:
    # create_newsapi_table in pg DB
    create_newsapi_table = PostgresOperator(
        task_id="create_news_tables",
        postgres_conn_id="airflow_db",
        sql="news_tables.sql",
    )