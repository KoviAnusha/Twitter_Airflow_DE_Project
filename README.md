# Twitter Data Pipeline using Apache Airflow (End to End)

![Data Architecture](./Data%20Architecture.png)

Steps:

1. Create a Twitter App on the Twitter Developer Portal and generate API KEY, API SECRET KEY, ACCESS TOKEN, and ACCESS SECRET TOKEN.
2. Write a Python code from which you should be able to access the Twitter API.
3. Check if you can access the Twitter API using that code.
4. Write a bash script in which you should call the above python file.
5. Write Python code to create a DAG, which you need to access the bash script.
6. Create an EC2 Instance and install airflow in that.
7. Access the EC2 instance via a web browser.
8. Deploy the DAG, python, and wrapper script into the airflow folder in the EC2 instance.
9. Run the DAG file in the airflow via a web browser and the data will be uploaded to S3.
10. Understand the data in the datasets
11. Build crawlers using AWS Glue
12. The data can be seen on Athena
13. Writing an AWS Glue Job using Python Shell Script
   - Connect to Redshift
   - Load data from CSV files in S3 to Redshift

