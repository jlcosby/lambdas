#create snapshots

from datetime import datetime

import boto3


def lambda_handler(event, context):

    ec2_client = boto3.client('ec2')
    regions = [region['RegionName']
               for region in ec2_client.describe_regions()['Regions']] 
#iterate across regions
    for region in regions:

        print('Instances in EC2 Region {0}:'.format(region))
        ec2 = boto3.resource('ec2', region_name=region)
#filter instances using the backup tag
        instances = ec2.instances.filter(
            Filters=[
                {'Name': 'tag:backup', 'Values': ['true']}
            ]
        )

        # ISO 8601 timestamp, i.e. 2019-01-31T14:01:58
        timestamp = datetime.utcnow().replace(microsecond=0).isoformat()
#create a snapshot of all instances with the backup tag that has the instance id, volume, and creation date
        for i in instances.all():
            for v in i.volumes.all():

                desc = 'Backup of {0}, volume {1}, created {2}'.format(
                    i.id, v.id, timestamp)
                print(desc)

                snapshot = v.create_snapshot(Description=desc)

                print("Created snapshot:", snapshot.id)
                
#Custom IAM Role: cloudwatch: allow create logs, create streams, write to events; ec2: create snapshot, create tags, delete snapshot, describe, modify snapshot attibute, reset snapshot attribute