import boto3

# Create an S3 client object
s3 = boto3.client('s3')

# Get the bucket's access control list
response = s3.get_bucket_acl(Bucket='firstpythonbuckete8a3f257-fbec-45b3-a9f1-835c629ab3c4')

# Parse the ACL response to get the authentication type for each grantee
for grant in response['Grants']:
    grantee = grant['Grantee']
    grantee_type = grantee.get('Type')
    if grantee_type == 'CanonicalUser':
        print('User ID:', grantee['ID'], 'is authenticated with AWS access keys')
    elif grantee_type == 'Group':
        group_uri = grantee.get('URI')
        if group_uri == 'http://acs.amazonaws.com/groups/global/AllUsers':
            print('User is authenticated as an anonymous user')
        elif group_uri == 'http://acs.amazonaws.com/groups/global/AuthenticatedUsers':
            print('User is authenticated as an authenticated user')
    else:
        print('Grantee:', grantee, 'has an unknown authentication type')

