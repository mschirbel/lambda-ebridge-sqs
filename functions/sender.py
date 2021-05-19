import boto3
import os


def lambda_handler(event, context):
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName=os.environ['SQS_NAME'])
    response = queue.send_message(
        MessageBody='demo-ebridge',
        MessageAttributes={
            'Author': {
                    'StringValue': 'Marcelo',
                    'DataType': 'String'
            }
        }
    )

    return response
