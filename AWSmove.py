import boto3
import time
s3 = boto3.resource('s3')
s3.meta.client.upload_file('image1.jpg', 'mybucketashkan123', 'image1.jpg')

time.sleep(30) # Sleep for 30 seconds

s3.meta.client.upload_file('image2.jpg', 'mybucketashkan123', 'image2.jpg')

time.sleep(30) # Sleep for 30 seconds

s3.meta.client.upload_file('image3.jpg', 'mybucketashkan123', 'image3.jpg')

time.sleep(30) # Sleep for 30 seconds

s3.meta.client.upload_file('image4.jpg', 'mybucketashkan123', 'image4.jpg')

time.sleep(30) # Sleep for 30 seconds

s3.meta.client.upload_file('image5.jpg', 'mybucketashkan123', 'image5.jpg')
