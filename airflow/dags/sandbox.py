from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from airflow.models.param import Param
from datetime import timedelta

user_input = {
        "user_sleep_timer": Param(30, type='integer', minimum=10, maximum=120),
        }

dag = DAG(
    dag_id="sandbox",
    schedule="0 0 * * *",   # https://crontab.guru/
    start_date=days_ago(0),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    tags=["labs", "damg7245"],
    params=user_input,
)

def print_with_sleep(**kwargs):
    from time import sleep
    print(f"Sleeping for {kwargs['dag_run'].conf['user_sleep_timer']} sec")
    #########
    text = "Sleeping"
    from PIL import Image, ImageDraw, ImageFont
    import numpy as np
    myfont = ImageFont.load_default()
    size = myfont.getsize(text)
    img = Image.new("1",size,"black")
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), text, "white", font=myfont)
    pixels = np.array(img, dtype=np.uint8)
    chars = np.array([' ','#'], dtype="U1")[pixels]
    strings = chars.view('U' + str(chars.shape[1])).flatten()
    print( "\n".join(strings))
    sleep(kwargs['dag_run'].conf['user_sleep_timer'])
    #########
    print("I am up now")


with dag:
    output_file = BashOperator(
    task_id="output_file",
    bash_command='echo "Hello from airflow" > /home/airflow/output_$(date "+%Y-%m-%d_%H:%M:%S").log'
    )

    clean_dir = BashOperator(
    task_id="clean_dir",
    bash_command='echo "Cleaning following files" ; ls -l /home/airflow/ ; rm -rf /home/airflow/*',
    )

    print_with_sleep = PythonOperator(   
    task_id='print_with_sleep',
    python_callable = print_with_sleep,
    provide_context=True,
    dag=dag,
    )


    clean_dir >> output_file