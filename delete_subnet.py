import boto3

subnet_id = 'subnet-0c274bd4fa4d9f66a'

ec2 = boto3.client('ec2')

ec2.delete_subnet(
    SubnetId=subnet_id,
)