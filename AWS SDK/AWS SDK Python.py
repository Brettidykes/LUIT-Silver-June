# Importing the boto3 library, which is the AWS SDK for Python, 
# used to interact with AWS services.
import boto3

# Create a session using the default configuration or explicitly 
# set credentials and region. The session stores AWS credentials 
# and settings for a specific environment. 
session = boto3.Session()

# Creating an S3 client using boto3's client method.
# A client provides low-level access to AWS S3, such as listing buckets, 
# uploading files, and other API operations. Clients are more focused 
# on performing individual operations with detailed control.
s3_client = boto3.client('s3')

# Creating another S3 client using the session object. 
# This can be useful when you have multiple profiles or want to work 
# with a specific session that has different credentials or region settings.
s3_client_with_session = session.client('s3')

# Creating an S3 resource using boto3's resource method.
# A resource provides high-level, object-oriented access to S3. 
# With a resource, you can work with S3 objects and buckets more easily 
# than with the client, using Python-like interactions (e.g., s3.Bucket('name')).
s3_resource = boto3.resource('s3')

# Creating another S3 resource using the session object.
# Similar to the client, this is useful if you want to use a specific session 
# for different credentials or configurations.
s3_resource_with_session = session.resource('s3')


#Use Case
    #Use client when:
        #You need fine-grained control over specific API operations.
        #You are performing actions like generating pre-signed URLs or handling low-level errors and responses.

    #Use resource when:
        #You prefer higher-level abstractions that align with Pythonic object interactions.
        #You are managing S3 objects and buckets in a way that simplifies your codebase and makes it more readable.