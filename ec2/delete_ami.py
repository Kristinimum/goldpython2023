import boto3

ec2 = boto3.client('ec2')

response = ec2.deregister_image(
    ImageId='ami-0a29d8e19f016bb74',
)
