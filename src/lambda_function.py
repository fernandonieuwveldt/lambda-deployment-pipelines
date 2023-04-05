import json
import requests

def lambda_handler(event, context):
    response = requests.get('https://api.github.com/fdnieuwveldt')
    return {
        'statusCode': response.status_code,
        'body': response.content
    }
