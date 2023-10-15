import boto3

session = boto3.session() #represents a single connection to AWS
s3 = boto3.client('s3') #client gives us more control with AWS so we will use over Resources.
s3 = session.client('s3')

s3 = boto3.resource('s3') # can be called from session but provides python way to deal with things
