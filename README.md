# Twitter Data Pipeline using Apache Airflow (End to End)

![Data Architecture](./Data%20Architecture.png)

Steps:

1. Create a Twitter App on Twitter Developer Portal and generate API KEY, API SECRET KEY, ACCESS TOKEN, and ACCESS SECRET TOKEN.
2. Write a python code from which you should be able to access the Twitter API.
3. Check if you are able to access the Twitter API using that code.
4. Write a bash script in which you should call the above python file.
5. Write a python code to create a DAG in which you need to access the bash script.
6. Create an EC2 Instance and install airflow in that.
7. Access the EC2 instance via web browser.
8. Deploy the DAG code, python code, and wrapper script into the airflow folder in EC2 instance.
9. Run the DAG file in the airflow via web browser and the data will be uploaded to S3.
10. Understand the data in the datasets
11. Build crawlers using AWS Glue
12. The data can be seen on Athena
13. Writing a AWS Glue Job using Python Shell Script
   - Connect to Redshift
   - Load data from CSV files in S3 to Redshift

