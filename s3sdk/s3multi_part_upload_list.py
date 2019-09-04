import logging
import boto
import sys
import os
import math
import boto.s3.connection
from boto.s3 import *
from boto.s3.connection import S3Connection
from filechunkio import FileChunkIO
import time

access_key = 'DI5N4CZDI21SGM7VD5K0'
secret_key = 'hiWlH8dx0rE2Ilda9qfiAxL2Pg8CEF77tD8qOuvl'

try:
	conn = boto.connect_s3(
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key,
        host = '172.16.103.18', port = 80,
        is_secure=False, calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )
except Exception, e:
    print "asdsad"

b = conn.get_bucket('wangz-bucket')
mp = b.list_multipart_uploads()
amp = b.get_all_multipart_uploads()
print('1111111111111111111111111111111111111111111111')
print(mp)
print('1111111111111111111111111111111111111111111111')
for m in amp:
    print(m.id)
    print(m.key_name)
    print(m.bucket_name)
    m.cancel_upload()
