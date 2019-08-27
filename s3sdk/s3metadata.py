import logging
import boto
import sys
import boto.s3.connection
from boto.s3 import *
from boto.s3.connection import S3Connection

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

src = conn.get_bucket('wangz-bucket')
#print("00000000000000000000000000000000000000000000000")
#for key in src.list():
#        print "{name}\t{size}\t{modified}".format(
#                name = key.name,
#                size = key.size,
#                modified = key.last_modified,
#              ) 
key = src.get_key('wangz')
print("00000000000000000000000000000000000000000000000")
print key.name
#key.set_remote_metadata({"expiresin": 3600}, {}, True)
#key.set_remote_metadata({'Content-Type': 'custom/type'}, {}, True)
print key.metadata
#print key.metadata['expires_in']
#key.get_contents_to_filename('filedir/test2')
