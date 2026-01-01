import boto3

# Create S3 client and resource once
s3_client = boto3.client('s3', region_name='ap-south-1')
s3_resource = boto3.resource('s3')

def create_bucket(s3_client, bucket_name, region):
    s3_client.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': region
        }
    )
    print("Bucket created successfully")

def show_buckets(s3_resource):
    for bucket in s3_resource.buckets.all():
        print(bucket.name)

def upload_backup(s3_client, file_name, bucket_name, key_name):
    with open(file_name, 'rb') as data:   # auto closes file
        s3_client.put_object(
            Bucket=bucket_name,
            Key=key_name,
            Body=data
        )
    print("Backup uploaded successfully")

# Variables
bucket_name = "python-backup-bucket-harshita"
region = "ap-south-1"
file_name = r"C:\Users\harsh\Desktop\Python-For-Devops\day-01\practice\backups\backup_2025-12-31.tar.gz"
key_name = "my-backup.tar.gz"

# Function calls
create_bucket(s3_client, bucket_name, region) 
show_buckets(s3_resource)
upload_backup(s3_client, file_name, bucket_name, key_name)

