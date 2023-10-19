import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances()

for reservation in response['Reservations']: 
    for instance in reservation['Instances']: 
        if instance['State']['Name'] == 'running' and instance['InstanceId'] != 'i-0a2624182a7373b45':
            print(instance['InstanceId']) 
            response = ec2.stop_instances(
            InstanceIds=[instance['InstanceId'], 
        ],
)

print(response)