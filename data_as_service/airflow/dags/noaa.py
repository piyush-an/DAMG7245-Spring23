#!/usr/bin/python3
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from airflow.models.param import Param
from datetime import timedelta
import pandas as pd
import os
from sqlalchemy import create_engine
from great_expectations_provider.operators.great_expectations import GreatExpectationsOperator
from great_expectations.data_context.types.base import (
    DataContextConfig,
    CheckpointConfig
)

base_path = "/opt/airflow/working_dir"
# data_dir = os.path.join(base_path, "News-Aggregator", "great_expectations", "data")
ge_root_dir = os.path.join(base_path, "great_expectations")
# report_dir = os.path.join(ge_root_dir, "uncommitted/data_docs/local_site/validations/nyt_raw_data_suite" )
BASE_URL = os.getenv("DB_URL", "postgresql://root:root@db:5432/noaa")

dag = DAG(
    dag_id="sandbox",
    schedule="0 0 * * *",   # https://crontab.guru/
    start_date=days_ago(0),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    tags=["labs", "damg7245"],
)


def get_station_nexrad(**kwargs):
    engine = create_engine(BASE_URL)
    engine.connect()
    cols = [
        (20, 51),    # Name
        (72, 75),    # ST
        (106, 116),  # Lat
        (116, 127)   # Lon
    ]
    df = pd.read_fwf(
        r"https://www.ncei.noaa.gov/access/homr/file/nexrad-stations.txt", colspecs=cols, skiprows=[1])
    df.to_sql(name='noaa_tbl', con=engine, index=False, if_exists='replace')


def export_noaa_db(**kwargs):
    engine = create_engine(BASE_URL)
    engine.connect()
    res = pd.read_sql_table("noaa_tbl", con=engine)
    res.to_csv(f"/opt/airflow/working_dir/data/noaa.csv",
               sep=',', index=False)


with dag:
    get_station_nexrad = PythonOperator(
        task_id='get_station_nexrad',
        python_callable=get_station_nexrad,
        provide_context=True,
        dag=dag,
    )

    export_noaa_db = PythonOperator(
        task_id='export_noaa_db',
        python_callable=export_noaa_db,
        provide_context=True,
        dag=dag,
    )

    ge_data_context_root_dir_with_checkpoint_name_pass = GreatExpectationsOperator(
        task_id="ge_data_context_root_dir_with_checkpoint_name_pass",
        data_context_root_dir=ge_root_dir,
        checkpoint_name="noaa_ck_v1",
        fail_task_on_validation_failure=False
    )

    # Flow
    get_station_nexrad >> export_noaa_db >> ge_data_context_root_dir_with_checkpoint_name_pass
