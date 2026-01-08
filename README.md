# PyS3Vault

**Automated Backup Uploads to AWS S3 from Local Machine**

PyS3Vault is a Python-based automation tool that securely uploads local backup files to AWS S3. It simplifies the backup process by automating bucket creation, file upload, and bucket listing, making it easy to maintain cloud backups with minimal effort.

---

## Features

- Automatically creates an S3 bucket if it doesn't exist.
- Uploads local backup files to the specified S3 bucket.
- Lists all buckets in your AWS account.
- Works seamlessly with Python and Boto3.
- Lightweight and easy to customize.

---

## How to Use

1. **Install dependencies**
```bash
pip install boto3

2. Update variables in s3_backup.py

  * bucket_name → Your desired S3 bucket name
  * region → AWS region (e.g., ap-south-1)
  * file_name → Path to your local backup file
  * key_name → Name of the file in S3

3. Run the script

   python scripts/s3_backup.py

