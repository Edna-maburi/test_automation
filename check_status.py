import boto3
import time
from botocore.exceptions import ClientError

# Initialize a boto3 client for IoT
iot_client = boto3.client('iot')

def check_job_status(job_id, thing_name):
    max_retries = 3
    retry_count = 0
    job_status = None
    last_status = None
    status_repeat_count = 0
    status_print_limit = 1 

    while retry_count < max_retries:
        try:
            iot_response = iot_client.describe_job_execution(
                jobId=job_id,
                thingName=thing_name
            )

            job_status = iot_response['execution']['status']
             
            if job_status != last_status:
                status_repeat_count = 0
                print(f"Meter {thing_name} status: {job_status}")
            elif status_repeat_count < status_print_limit:
                status_repeat_count += 1
                print(f"Meter {thing_name} status: {job_status}")

            last_status = job_status    

            if job_status in ['SUCCEEDED', 'FAILED', 'REMOVED', 'REJECTED', 'TIMED_OUT', 'CANCELED']:
                break

        except ClientError as e:
            error_code = e.response['Error']['Code']
            error_message = e.response['Error']['Message']

            if error_code == 'ResourceNotFoundException':
                print(f"Job execution not found: {error_message}. Retrying...")
                retry_count += 1
                time.sleep(5)
            else:
                print(f"Error checking job status: {error_message}")
                return

    if job_status is None:
        print("Failed to retrieve job status after retries")
