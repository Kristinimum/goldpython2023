import boto3

def filter_objects_extension(client, bucket, extension):
    keys = []
    response = client.list_objects_v2(Bucket=bucket)
    for content in response["Contents"]:
        if(extension in content["Key"][-(len(extension)):]): #doing it this way will only include files that end with .txt isntaead of anything with txt in it.
            keys.append(content["Key"])

    return keys
    
def list_objects_keys(client, bucket, prefix=""):
    keys = []
    response = client.list_objects_v2(Bucket=bucket, Prefix=prefix)
    for content in response["Contents"]:
            keys.append(content["Key"])

    return keys    


if __name__== '__main__':
    s3 = boto3.client('s3')

    response = list_objects_keys(s3, "kmaxwell-boto3-10152023", "folder/")
    print(response)
#s3.list_objects_v2(Bucket="kmaxwell-boto3-10152023") #Prefix="folder/folder_a/")
    response = filter_objects_extension(s3, "kmaxwell-boto3-10152023", "/")
    print(response)

    