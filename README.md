# SAP S3 Upload Demo

This project demonstrates a simple Python workflow for creating a timestamped file, uploading it to an Amazon S3 bucket, and cleaning up the local copy afterward. It is designed as a lightweight example for working with AWS S3 from a Python environment and is useful for testing bucket access, IAM credentials, and file transfer automation.

## What this project does

The main script in `source/S3-Put.py` performs the following steps:

1. Creates a new text file with a timestamped name such as `log_2026-10-17_08-57-19.txt`
2. Writes a short success message into the file
3. Uploads the file to a configured S3 bucket using the AWS SDK for Python (`boto3`)
4. Removes the local temporary file after upload to keep the working folder clean

This makes it a practical example for basic S3 object upload automation in a development or demo environment.

## Project structure

- `source/S3-Put.py` - Main upload script
- `README.md` - Project overview and usage notes

## Requirements

- Python 3
- `boto3`
- Valid AWS credentials configured on the system or in the AWS CLI profile

## AWS configuration

The script uses `boto3.client('s3')`, which automatically reads credentials from common AWS configuration locations such as:

- `~/.aws/credentials`
- environment variables such as `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
- instance metadata or other AWS credential providers when available

Ensure the AWS identity used by the script has permission to upload files to the target bucket.

## Example usage

From the project root, run:

```bash
python source/S3-Put.py
```

The script currently uploads to the bucket named:

```python
'amzn-s3-sap-demo'
```

The file name used in S3 is the same as the local timestamped file name, so the S3 object name is easy to trace and audit.

## Notes

- The function `createFileWithTimestamp()` generates a unique file name to avoid overwriting previous test uploads.
- The upload logic catches common AWS and file-related errors and prints helpful messages.
- `cleanup()` removes files created by the script after the upload completes.

## Summary

This work creates a compact and reusable S3 upload example that can be extended for real data movement, SAP integration testing, or cloud file transfer workflows. It demonstrates the core pattern of generating a file locally, transferring it to S3, and cleaning up after the run.
