import boto3

ec2 = boto3.client('ec2')

response = ec2.delete_security_group(
    GroupId='sg-000ee1dd58f4a0e80',
)

print(response)