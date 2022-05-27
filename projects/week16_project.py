#Create a standard sqs queue using python and boto3

import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Create the queue. This returns an SQS.Queue instance
queue = sqs.create_queue(QueueName='current-time')

# You can now access identifiers and attributes
print(queue.url)
