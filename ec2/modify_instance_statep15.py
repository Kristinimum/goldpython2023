import boto3

instance_id = "i-0af9456eb5897d222"

ec2 = boto3.client('ec2')

response = ec2.stop_instances(
    InstanceIds=[
        instance_id,
    ],
)

print(response)