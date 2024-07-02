import boto3
import json

# Initialize a boto3 client for API Gateway
api_client = boto3.client('apigateway')

def call_api(resource, thing_name):
    api_id = 'yqb5pgwwsc'
    resource_id = resource['resource_id']
    payload = resource['payload']
    http_method = 'POST'
    path_with_query_string = resource['path_with_query_string']
    
    try:
        response = api_client.test_invoke_method(
            restApiId=api_id,
            resourceId=resource_id,
            httpMethod=http_method,
            pathWithQueryString=path_with_query_string,
            body=json.dumps(payload)
        )
        
        status = response['status']
        body_str = response['body']
        
        try:
            body = json.loads(body_str)
            job_id = body.get('jobId')
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse JSON response: {body_str}") from e
        except AttributeError:
            raise ValueError(f"Failed to get 'jobId' from API response body: {body_str}")
        
        if not job_id:
            raise ValueError("Job ID not found in the API response")
        
        print(f"API Status: {status}")
        print(f"Job ID: {job_id}")
        
        return job_id
    
    except Exception as e:
        print(f"Error calling API Gateway for {thing_name}: {e}")
        return None
