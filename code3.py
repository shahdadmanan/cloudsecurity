import boto3

# Create an S3 client object
s3 = boto3.client('s3')

# Get the bucket's encryption configuration
response = s3.get_bucket_encryption(Bucket='firstpythonbuckete8a3f257-fbec-45b3-a9f1-835c629ab3c4')
print(response)
print(".........................................................")
# Get the bucket's access control list
response = s3.get_bucket_acl(Bucket='firstpythonbuckete8a3f257-fbec-45b3-a9f1-835c629ab3c4')
print(response)
print(".........................................................")
# Get the bucket's public access block configuration
try:
    response = s3.get_public_access_block(Bucket='firstpythonbuckete8a3f257-fbec-45b3-a9f1-835c629ab3c4')
    print(response)
except:
    print("PUBLIC ACCESS BLOCK CONFIGURATION NOT FOUND")
    
print(".........................................................")
# Get the bucket's server-side encryption configuration
response = s3.get_bucket_encryption(Bucket='firstpythonbuckete8a3f257-fbec-45b3-a9f1-835c629ab3c4')
print(response)
print(".........................................................")
# Get the bucket's logging configuration
response = s3.get_bucket_logging(Bucket='firstpythonbuckete8a3f257-fbec-45b3-a9f1-835c629ab3c4')
print(response)
print(".........................................................")
# Get the bucket's default retention configuration
try: 
    response = s3.get_object_lock_configuration(Bucket='firstpythonbuckete8a3f257-fbec-45b3-a9f1-835c629ab3c4')
    print(response)
except:
    print("OBJECT LOCK CONFIGURATION DOES NOT EXIST")

