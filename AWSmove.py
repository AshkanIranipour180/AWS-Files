import boto3
s3 = boto3.resource('s3')
s3.meta.client.upload_file('image1.jpg', 'mybucketashkan123', 'image1.jpg')
