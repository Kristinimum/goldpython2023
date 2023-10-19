
import boto3

ec2=boto3.resource('ec2')

instances=ec2.instances.filter(Filters = [{'Name': 'instance-state-name', 'Values': ['running']}, {'Name':'tag:'Environment', 'Values':['Devoloper']}])

for ins in instances:
  try:
      ins.stop()
      print(f'{instance} stopped')
  except:
      print(f'Error stopping {instance}')