import boto3

internet_gateway_id = 'igw-0d295bd6deaa36e48'

ec2 = boto3.client('ec2')

ec2.delete_internet_gateway(
    InternetGatewayId=internet_gateway_id,
)
