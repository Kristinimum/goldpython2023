import boto3

internet_gateway_id = 'igw-0d295bd6deaa36e48'
vpc_id = 'vpc-0a3592ea98c275984'

ec2 = boto3.client('ec2')

ec2.detach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id,
)
