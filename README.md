# redshift-pipeline
This project demonstrates a data pipeline using Mage AI to transfer data from a CSV file to AWS S3 and then load it into an AWS Redshift cluster. The setup leverages Docker Compose for container orchestration, ensuring a seamless development and deployment experience.

Features
Mage AI Integration: Utilize Mage AI for efficient data processing and pipeline management.
AWS S3 Storage: Securely upload CSV data to AWS S3 for scalable storage.
AWS Redshift: Load data from S3 into Redshift for robust data warehousing and analytics.
Dockerized Environment: Simplified deployment using Docker and Docker Compose.
Configuration via .env File: Easy environment management and configuration.
Project Structure
mage_pipeline/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── pipeline/
    ├── __init__.py
    ├── pipeline.py
    └── config.py
└── taxidata.csv


Here's a suggested GitHub description for your project:

Data Pipeline with Mage AI, AWS S3, and Redshift
Overview
This project demonstrates a data pipeline using Mage AI to transfer data from a CSV file to AWS S3 and then load it into an AWS Redshift cluster. The setup leverages Docker Compose for container orchestration, ensuring a seamless development and deployment experience.

Features
Mage AI Integration: Utilize Mage AI for efficient data processing and pipeline management.
AWS S3 Storage: Securely upload CSV data to AWS S3 for scalable storage.
AWS Redshift: Load data from S3 into Redshift for robust data warehousing and analytics.
Dockerized Environment: Simplified deployment using Docker and Docker Compose.
Configuration via .env File: Easy environment management and configuration.
Project Structure

mage_pipeline/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── pipeline/
    ├── __init__.py
    ├── pipeline.py
    └── config.py
└── taxidata.csv
Prerequisites
Docker and Docker Compose installed on your machine.
AWS credentials with necessary permissions for S3 and Redshift.
A running AWS Redshift cluster.
Setup
Clone the repository:


git clone https://github.com/yourusername/mage_pipeline.git
cd mage_pipeline
Configure environment variables:

Create and populate the .env file with your AWS and Redshift configurations.

env

AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_S3_BUCKET=your_s3_bucket
REDSHIFT_HOST=your_redshift_host
REDSHIFT_PORT=5439
REDSHIFT_DB=your_database
REDSHIFT_USER=your_user
REDSHIFT_PASSWORD=your_password
Build and run the Docker container:

sh
Copy code
docker-compose build
docker-compose up
Usage
Pipeline Execution: The pipeline reads data from taxidata.csv, uploads it to S3, and then loads it into Redshift.
Testing Connection: Use the test_connection.py script to verify Redshift

