import boto3

route_table_id = 'rtb-04e483cb2e40eb519'
internet_gateway_id = 'igw-0d295bd6deaa36e48'

ec2 = boto3.client('ec2')

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway_id,
    RouteTableId=route_table_id,
)