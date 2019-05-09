import json

def lambda_handler(event, context):
    print(json.dumps(event))
    #x = 2 / 0
    return {
        "statusCode": 200,
        "body": json.dumps('Priority')
    }