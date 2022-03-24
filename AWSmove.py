import boto3

s3_client = boto3.client('s3', region_name='us-east-1', aws_access_key_id=vockey)

s3 = boto3.resource('s3')
s3.meta.client.upload_file('image1.jpg', 'mybucketashkan123', 'image1.jpg')
