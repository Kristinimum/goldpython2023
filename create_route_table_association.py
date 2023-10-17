import boto3

route_table_id = 'rtb-04e483cb2e40eb519'
subnet_id = 'subnet-0c274bd4fa4d9f66a'

ec2 = boto3.client('ec2')

association = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id,
)

print(association["AssociationId"])