import boto3

vpc_id = 'vpc-0a3592ea98c275984'

ec2 = boto3.client('ec2')

ec2.delete_vpc(
    VpcId=vpc_id,
)
