# This program is to download the file from a bucket 
# @Author : Akshay Patil

import boto
from boto.s3.connection import S3Connection
from boto.s3.key import Key


# give bucket name to search :- 
conn = S3Connection ("", "") # Your Access Keys Here 

bucket = conn.get_bucket("custom-bucket-from-python")

k = Key(bucket)
k.key = "Filename1"
print "Size" + str(k.size)

#TODO : Change the file save path here
k.get_contents_to_filename("/home/akshay/Desktop/gets34.jpg")
print "Downloading the file"


