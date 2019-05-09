import json
import boto3
import os

dbclient = boto3.client("dynamodb")
table_name = os.environ['TABLE_NAME']

def lambda_handler(event, context):
    # TODO implement
    print(json.dumps(event))
    name = event['message']
    email = event['email']
    print("name = {}, email = {}".format(name, email))
    response = save_person(email, name)
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }


def save_person(email, name):
    item = create_item(email, name)
    response = add_item_to_dynamodb_table(table_name, item)
    return response
    
def create_item(email, name):
    item = {
    'email': {'S': email},
    'name': {'S': name}
    }
    return item
    
def add_item_to_dynamodb_table(table, item):
    response = dbclient.put_item(TableName=table, Item=item)
    return(response)