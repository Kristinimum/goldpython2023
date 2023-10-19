import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances()

devtag = { "Key":"Environment", "Value":"Dev"}

reservations = response['Reservations']

for reservation in reservations:
    instances = reservation['Instances']
    
    for instance in instances:
        if (devtag in instance['Tags'] and 'running' in instance['State']['Name']):
            print(instance['InstanceId'])
            ec2.stop_instances(InstanceIds=[instance['InstanceId']])
