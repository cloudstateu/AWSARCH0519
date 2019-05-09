import json
import os
import boto3

sqs_client = boto3.client('sqs')

def lambda_handler(event, context):
    
    priority_ip_address = os.environ['priority_ip_address']
    priority_queue_url = os.environ['priority_queue_url']
    standard_queue_url = os.environ['standard_queue_url']
    
    print(json.dumps(event))
    headers = event.get('headers')
    if headers is not None:
        x_forwarded_for = headers.get('X-Forwarded-For')
        if x_forwarded_for is not None:
            ip_addresses  = x_forwarded_for.split(',')
            if any(priority_ip_address in s for s in ip_addresses):
                sqs_client.send_message(
                    QueueUrl=priority_queue_url,
                    MessageBody='priority')
                
                return {
                    "statusCode": 200,
                    "body": json.dumps('Cheers from AWS Lambda!!')
                }
            else:
                sqs_client.send_message(
                    QueueUrl=standard_queue_url,
                    MessageBody='standard')
                return {
                    "statusCode": 200,
                    "body": json.dumps('Standard request')
                }