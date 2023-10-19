import boto3 #for all boto3 Python files

ec2 = boto3.client('ec2') #creates our ec2 client

response = ec2.describe_instances() #describes ec2 instances that are in your console

for reservation in response['Reservations']: 
    for instance in reservation['Instances']:   # parsing in reservations to find running instances
        if instance['State']['Name'] == 'running' and instance['InstanceId'] != 'i-0a2624182a7373b45': #prevents our Cloud9 instance from stopping
            print(instance['InstanceId']) #Prints instances id that will be stopped
            response2 = ec2.stop_instances(
            InstanceIds=[instance['InstanceId'], #stops the running instances from above
        ],
)

print(response2) #prints success code 200, the instance has stopped