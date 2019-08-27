import logging
import boto
import sys
import os
import math
import boto.s3.connection
from boto.s3 import *
from boto.s3.connection import S3Connection
from filechunkio import FileChunkIO

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
source_path = './local-50M-file'

source_size = os.stat(source_path).st_size
mul_key = 'HEHE'

header = {
    'x-amz-meta-gang': 'Yang Honggang'
}


mp = b.initiate_multipart_upload(mul_key)

chunk_size = 20971520
chunk_size = 2048
chunk_count = int(math.ceil(source_size / float(chunk_size)))

for i in range(chunk_count):
    offset = chunk_size * i
    bytes = min(chunk_size, source_size - offset)
    with FileChunkIO(source_path, 'r', offset=offset,bytes=bytes) as fp:
        print("0000000000000000(chunk_count:%d)0000000000000(tell:%d)000000000000000000" % (chunk_count, fp.tell()))
        print(type(fp))
        mp.upload_part_from_file(fp, part_num=i + 1)

print "before complete"
#mp.complete_upload()
