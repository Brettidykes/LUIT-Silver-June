import boto3

s3 = boto3.client('s3')

#with open("C:/Users/brett/OneDrive/Documents/GitHub/LUIT-Silver-June/AWS SDK/test_text.txt", 'rb') as f:
    #s3.put_object(Bucket="dykes-boto3-092624", Key="test_text.txt", Body =f, ContentType="text/plain")

s3.upload_file('C:/Users/brett/OneDrive/Documents/GitHub/LUIT-Silver-June/AWS SDK/test_text.txt', 'dykes-boto3-092624', 'test_text_upload.txt', ExtraArgs={'ContentType':'text/plain'})