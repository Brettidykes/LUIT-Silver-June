import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='dykes-boto3-092624'
)

print(response)