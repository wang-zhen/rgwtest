import logging
import boto
import sys
import os
import math
import boto.s3.connection
from boto.s3 import *
from boto.s3.connection import S3Connection
from filechunkio import FileChunkIO
from io import BytesIO

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

mul_key = 'HEHE'

header = {
    'x-amz-meta-gang': 'Yang Honggang'
}

mp = b.initiate_multipart_upload(mul_key)

data = "file1"
fp = BytesIO(data)
mp.upload_part_from_file(fp, part_num=1)
data = "file2"
fp = BytesIO(data)
print("000000(tell:%d)000000" % (fp.tell()))
#print("000000(bytes:%d)000000" % (fp.bytes))
#print("000000(bytes:%s)000000" % (fp.read()))
#print("000000(offset:%s)000000" % (fp.offset))
#mp.upload_part_from_file(fp, part_num=2)

print "before complete"
print type(fp)
#mp.complete_upload()
