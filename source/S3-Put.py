from datetime import datetime

import boto3
from botocore.exceptions import NoCredentialsError, ClientError

def upload_to_s3(local_file, bucket_name, s3_file_name=None):
    # If S3 object name was not specified, use local_file name
    if s3_file_name is None:
        s3_file_name = local_file

    # Initialize the S3 client
    # It automatically picks up credentials from ~/.aws/credentials or environment variables
    s3 = boto3.client('s3')

    try:
        print(f"Uploading {local_file} to {bucket_name}/{s3_file_name}...")
        
        s3.upload_file(local_file, bucket_name, s3_file_name)
        print("Upload successful!")
        return True
        
    except FileNotFoundError:
        print(f"The file {local_file} was not found.")
        return False
    except NoCredentialsError:
        print("Credentials not available. Please configure your AWS keys.")
        return False
    except ClientError as e:
        print(f"An AWS client error occurred: {e}")
        return False

def createFileWithTimestamp():
    from datetime import datetime

    # 1. Get the current date and time
    now = datetime.now()

    # 2. Format the timestamp safely for file systems (YYYY-MM-DD_HH-MM-SS)
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

    # 3. Create the filename
    filename = f"log_{timestamp}.txt"

    # 4. Open and write to the file
    with open(filename, "w") as file:
        file.write("File created successfully with a timestamped filename.")

    print(f"Created file: {filename}")
    
    return filename

def cleanup():
    import os
    # Remove the created file after upload to keep the environment clean
    for file in os.listdir('.'):
        if file.startswith("log_") and file.endswith(".txt"):
            os.remove(file)
            print(f"Removed file: {file}")
            
filename = createFileWithTimestamp()
upload_to_s3(filename, 'amzn-s3-sap-demo', filename)
cleanup()
