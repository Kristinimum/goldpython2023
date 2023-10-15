import boto3

s3 = boto3.client('s3')

s3.put_object(Bucket="kmaxwell-boto3-10152023", Key="folder/folder_c/test_text_string.txt", Body="folder created with boto3", ContentType="text/plain")
