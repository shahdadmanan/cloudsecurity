import boto3
import uuid
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')


def create_temp_file(size, file_name, file_content):
    random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])
    with open(random_file_name, 'w') as f:
        f.write("THIS IS A TEST... ONE STEP AT A TIME")
    return random_file_name

first_file_name = create_temp_file(300, 'firstfile.txt', 'f') 

first_bucket = s3_resource.Bucket(name="firstpythonbuckete8a3f257-fbec-45b3-a9f1-835c629ab3c4")
first_object = s3_resource.Object(
    bucket_name="firstpythonbuckete8a3f257-fbec-45b3-a9f1-835c629ab3c4", key=first_file_name)
    
s3_resource.Bucket("firstpythonbuckete8a3f257-fbec-45b3-a9f1-835c629ab3c4").upload_file(
    Filename=first_file_name, Key=first_file_name)
