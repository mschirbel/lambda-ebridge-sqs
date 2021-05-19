import os
import json


def lambda_handler(event, context):
    sqs_name = os.environ['SQS_NAME']
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "SQSName ": sqs_name,
            "m_id": event['Records'][0].messageId
        })
    }
