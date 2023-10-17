import boto3

route_table_id = 'rtb-04e483cb2e40eb519'

ec2 = boto3.client('ec2')

ec2.delete_route_table(
    RouteTableId=route_table_id,
)
