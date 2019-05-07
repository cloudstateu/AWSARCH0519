import json
import boto3
import os

s3Client = boto3.client('s3')
snsClient = boto3.client('sns')

phone_number = os.environ['phone_number']
sender_id = os.environ['sender_id']

def lambda_handler(event, context):
    print(json.dumps(event))
    number = phone_number
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        print(bucket_name)
        file_name = record['s3']['object']['key']
        print(file_name)
        url = s3Client.generate_presigned_url('get_object', Params = {'Bucket': bucket_name, 'Key': file_name}, ExpiresIn = 3600)
        print(url)
        snsClient.publish(PhoneNumber = number,
            Message=url ,
            MessageAttributes={
                'AWS.SNS.SMS.SenderID': {
                'DataType': 'String',
                'StringValue': sender_id
                }
            }
        )


