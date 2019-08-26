import botocore
import boto3
import botocore
import logging
from boto3.session import Session
import boto
import boto.s3.connection

access_key = '16Q6469KTFTC0VJ19037W'
secret_key = 'Vhu1Ox5e1BMf5fZXo2xFrKK750tjZlhXXySkHRPw'
s3_host = 'http://127.0.0.1:7480'

#session = Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key)

#s3 = session.resource('s3', endpoint_url='http://127.0.0.1:7480')

#for bucket in s3.buckets.all():
#     print('bucket name:%s' % bucket.name)

s3client = boto3.client('s3',aws_secret_access_key = secret_key,aws_access_key_id = access_key,endpoint_url = s3_host)
#s3client = boto3.resource('s3',
#                        endpoint_url=s3_host,
#                        aws_access_key_id=access_key,
#                        aws_secret_access_key=secret_key)

'''
conn = boto.connect_s3(
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key,
        host = '127.0.0.1',
        #is_secure=False,               # uncomment if you are not using ssl
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )
'''
#response = s3client.list_buckets()
#response = s3client.list_buckets()
#for bucket in response['Buckets']:
#	  print "Listing owned buckets returns => {0} was created on {1}\n".format(bucket['Name'], bucket['CreationDate'])
