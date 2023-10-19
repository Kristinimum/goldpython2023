import json
import boto3

region='us-east-1'
instances=['i-0e6d3d5d1647c0c85']

def lambda_handler(event, context):
   ec2 = boto3.client('ec2' , region_name=region)
   ec2.stop_instances(instanceIds=instances)
   print('You have now stopped your instances')