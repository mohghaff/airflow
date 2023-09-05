
Table of Contents
Introduction
Project Overview
Project Structure
Airflow DAGs
1. Airflow DAG with BashOperator
2. Airflow DAG with PythonOperator and XComs
3. Airflow TaskFlow API
4. Airflow Catchup and Backfill
5. Schedule Airflow DAG with Cron Expression
6. Airflow Connection and PostgresOperator
7. Python Dependencies via Airflow Docker Image Extending and Customizing
8. AWS S3 Key Sensor Operator
9. Airflow Hooks S3 PostgreSQL

Introduction
Welcome to the Airflow Project! This repository contains various Airflow DAGs and related components that helped me to learn and practice working with Apache Airflow. Apache Airflow is an open-source platform used for orchestrating, scheduling, and monitoring workflows.

Project Overview
This project provides examples of different Airflow DAGs and features, including BashOperator, PythonOperator, TaskFlow API, catchup and backfill strategies, cron expressions for scheduling, connections, PostgreSQLOperator, Docker image customization, AWS S3 integration, and more. Each section below corresponds to a specific topic.



Airflow DAGs
1. Airflow DAG with BashOperator
my_first_dag.py
This DAG demonstrates the use of the BashOperator to run a simple Bash command as a task within the workflow.

2. Airflow DAG with PythonOperator and XComs
python_dag.py
This DAG showcases the use of the PythonOperator and XComs in Apache Airflow. PythonOperators execute Python functions as tasks, while XComs allow task-to-task communication. You can share data between tasks using XComs, making it a powerful tool for workflow coordination. This example highlights these features, demonstrating their utility within your Airflow workflows

3. Airflow TaskFlow API
dags_with_taskflow_api.py
This DAG showcases the TaskFlow API, an alternative way to define workflows in Airflow using Python classes and methods. It offers greater flexibility and organization compared to traditional Operator-based DAGs.

4. Airflow Catchup and Backfill
dag_with_catchup_backfill.py
This DAG illustrates the concepts of catchup and backfill in Airflow. It demonstrates how to rerun or backfill historical data for tasks using the catchup configuration and the airflow backfill command.

5. Schedule Airflow DAG with Cron Expression
dag_with_cron_expressions.py
This DAG demonstrates how to schedule a workflow using a Cron expression. You can set up complex scheduling patterns by specifying a Cron expression, providing fine-grained control over when your DAG runs.

6. Airflow Connection and PostgresOperator
dags_with_postgres_operator.py
This DAG showcases the use of Airflow connections and the PostgresOperator to interact with a PostgreSQL database. You can define database connections in Airflow and securely access them in your DAGs.

7. Python Dependencies via Airflow Docker Image Extending and Customizing
dags_with_python_dependencies.py
docker/Dockerfile
docker/requirements.txt
This section demonstrates how to extend and customize the Airflow Docker image to include specific Python dependencies for your DAGs. You can build a custom Docker image with your project's requirements and use it to run your DAGs.

8. AWS S3 Key Sensor Operator
dags_with_minio_s3.py
This DAG shows how to use the S3KeySensor operator to wait for a specific file or object to appear in an AWS S3 bucket. It's useful for scenarios where you want to trigger a task when new data becomes available in S3.

9. Airflow Hooks S3 PostgreSQL
dags_with_posgres_hooks.py
This DAG combines multiple concepts, including using Airflow hooks to interact with AWS S3 and PostgreSQL. It demonstrates how to perform operations such as uploading files to S3 and querying data from a PostgreSQL database within your workflow.