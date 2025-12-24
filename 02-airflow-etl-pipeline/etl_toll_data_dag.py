# import the libraries

from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow.models import DAG
# Operators; you need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago

#defining DAG arguments

# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'Airflow_Si_Thu',
    'start_date': days_ago(0),
    'email': ['sithudummy123@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# defining the DAG

# define the DAG
dag = DAG(
    dag_id='ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule_interval=timedelta(days=1),
)

# define the tasks

# define the first task
unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='tar -xzf /home/project/airflow/dags/finalassignment/tolldata.tgz -C /home/project/airflow/dags/finalassignment',
    dag=dag,
)

# Create a task named extract_data_from_csv to extract the fields Rowid, Timestamp, Anonymized Vehicle number, and Vehicle type from the vehicle-data.csv file and save them into a file named csv_data.csv.
# define the second task
extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command='cut -d"," -f1,2,3,4 /home/project/airflow/dags/finalassignment/vehicle-data.csv > /home/project/airflow/dags/finalassignment/csv_data.csv',
    dag=dag,
)

# Create a task named extract_data_from_tsv to extract the fields Number of axles, Tollplaza id, and Tollplaza code from the tollplaza-data.tsv file and save it into a file named tsv_data.csv.
# define the third task
extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command="cut -d$'\t' -f5,6,7 /home/project/airflow/dags/finalassignment/tollplaza-data.tsv > /home/project/airflow/dags/finalassignment/tsv_data.csv",
    dag=dag,
)

# Create a task named extract_data_from_fixed_width to extract the fields Type of Payment code, and Vehicle Code from the fixed width file payment-data.txt and save it into a file named fixed_width_data.csv.
# define the fourth task
extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command='cut -c11-13,15-17 /home/project/airflow/dags/finalassignment/payment-data.txt > /home/project/airflow/dags/finalassignment/fixed_width_data.csv',
    dag=dag,
)

# Create a task named consolidate_data to consolidate data extracted from previous tasks. This task should create a single csv file named extracted_data.csv by combining data from the following files:
# csv_data.csv
# tsv_data.csv
# fixed_width_data.csv
# define the fifth task
consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command="paste \
                    /home/project/airflow/dags/finalassignment/csv_data.csv \
                    /home/project/airflow/dags/finalassignment/tsv_data.csv \
                    /home/project/airflow/dags/finalassignment/fixed_width_data.csv \
                    > /home/project/airflow/dags/finalassignment/extracted_data.csv",
    dag=dag,
)

# Create a task named transform_data to transform the vehicle_type field in extracted_data.csv into capital letters and save it into a file named transformed_data.csv in the staging directory.
# define the sixth task
transform_data = BashOperator(
    task_id='transform_data',
    bash_command="""
    cut -d',' -f1-3 /home/project/airflow/dags/finalassignment/extracted_data.csv > /tmp/part1.csv &&
    cut -d',' -f4 /home/project/airflow/dags/finalassignment/extracted_data.csv | tr '[:lower:]' '[:upper:]' > /tmp/part2.csv &&
    paste -d',' /tmp/part1.csv /tmp/part2.csv > /home/project/airflow/dags/finalassignment/staging/transformed_data.csv
    """,
    dag=dag,
)

# task pipeline
unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data