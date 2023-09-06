Twitter ETL Project Documentation

Overview
This documentation provides an overview of the Twitter ETL (Extract, Transform, Load) project. The project is designed to collect information about Twitter users and store it in an Amazon S3 bucket. It utilizes Tweepy, a Python library for accessing the Twitter API, and Apache Airflow for scheduling and automating the ETL process.

Project Components
Tweepy: Tweepy is used to interact with the Twitter API and fetch user data.

Pandas: Pandas is used for data manipulation and to create a DataFrame containing Twitter user information.

Amazon S3: Amazon S3 is used to store the collected data.

Apache Airflow: Apache Airflow is used to schedule and execute the ETL process on an EC2 instance.

Prerequisites
Before running the project, ensure that you have the following prerequisites in place:

Access to an AWS account with permissions to create and manage an Amazon S3 bucket.
An AWS EC2 instance set up with appropriate IAM roles or AWS access keys and secret keys.
Project Setup
Step 1: Installation
Install the necessary Python libraries on your EC2 instance:


Step 2: Twitter API Credentials
Obtain Twitter API credentials (consumer key, consumer secret, access token, and access token secret) by creating a Twitter Developer App.

Step 3: Python Script
Create a Python script (twitter_etl.py) that fetches Twitter user data using Tweepy and stores it in an Amazon S3 bucket.


Step 4: Apache Airflow DAG
Create an Apache Airflow DAG (twitter_dag.py) to schedule and run the ETL process daily.


Step 5: Airflow Configuration
Ensure that Apache Airflow is correctly configured with the necessary connections and environment variables for AWS credentials.

Execution
Start your Apache Airflow scheduler to trigger the ETL process daily.

The run_twitter_etl function will fetch Twitter user data and store it in the specified Amazon S3 bucket.

Conclusion
This project demonstrates how to collect Twitter user data using Tweepy, store it in Amazon S3, and schedule the ETL process using Apache Airflow. 

