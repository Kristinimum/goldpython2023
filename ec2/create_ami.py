import boto3

ec2 = boto3.client('ec2')

response = ec2.create_image(
    InstanceId='i-0f43d8ae720e9073a',
    Name='Go to Ami',
)

print(response["ImageId"])