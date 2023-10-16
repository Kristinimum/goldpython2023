import boto3
import os
from list_objects import list_objects_keys
#this is a function to download a single object
def download_single_object(client, bucket, key, Filename):
    client.download_file(bucket, key, Filename)

if __name__== '__main__':
   
    bucket = 'kmaxwell-boto3-10152023'
    key = 'test_text_string.txt'
    Filename = 'test_text_string.txt'

    s3 = boto3.client('s3')

    keys = list_objects_keys(s3, bucket, prefix="folder/")
    
    for key in keys:
        if '/' == key[-1]:
            try:
                os.mkdir(key)
            except:
                pass
        else:
            download_single_object(s3, bucket, key, key)