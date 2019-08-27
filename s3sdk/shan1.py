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

source_path = './local-10M-file'
#source_path = './local-40-file'

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
header = {
    'x-amz-meta-gang': 'Yang Honggang'
}

mul_key = 'ceshi'
mp = b.initiate_multipart_upload(mul_key)

''' 50M'''
''' 40'''
source_size = os.stat(source_path).st_size

''' 5M'''
chunk_size = 1048576*5

''' 3'''
chunk_count = int(math.ceil(source_size / float(chunk_size)))
print(source_size)
print(chunk_size)
print(chunk_count)

'''
en = open(source_path, 'rw')
str1 = en.read(chunk_size)
str2 = en.read(chunk_size)
data1 =  BytesIO(str1)
data2 =  BytesIO(str2)
mp.upload_part_from_file(data1, part_num=1)
mp.upload_part_from_file(data2, part_num=2)
mp.complete_upload()

print(type(data1))
print(type(data2))
sys.exit(0)
'''

i=0
for i in range(chunk_count):
    print('11111111111111111111111111')
    offset = chunk_size * i
    bytes = min(chunk_size, source_size - offset)
    with FileChunkIO(source_path, 'r', offset=offset,bytes=bytes) as fp:
        print("000000(tell:%d)000000" % (fp.tell()))
        print("000000(bytes:%d)000000" % (fp.bytes))
        #print("000000(bytes:%s)000000" % (fp.read()))
        print("000000(offset:%s)000000" % (fp.offset))
        mp.upload_part_from_file(fp, part_num=i + 1 +1)

print "before complete"
mp.complete_upload()
