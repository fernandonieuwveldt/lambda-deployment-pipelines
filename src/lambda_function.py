import json


def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello, I was deployed from a github action'
    }
