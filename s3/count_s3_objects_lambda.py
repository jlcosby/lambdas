#get count of s3 bucket objects with lambda using boto3
import boto3
import json

s3 = boto3.client('s3')

def lambda_handler(event, context):
    
    response = s3.list_objects(Bucket='bucketname')
    
    Contents = response['Contents']
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('This bucket has ' + str(len(Contents)) + " objects!")
    }
