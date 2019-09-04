import logging
import boto
import sys
import boto.s3.connection
from boto.s3 import *
from boto.s3.connection import S3Connection

access_key = '5QJEDSQUFW07UMSCEAML'
secret_key = 'Kdr7OFkDtQlIM8cA3iDAdwR7Hn4NqWtxO6PAJDsD'

try:
	conn = boto.connect_s3(
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key,
        host = '172.16.103.18', port = 80,
        is_secure=False, calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )
except Exception, e:
    print "asdsad"
	#logging.error("wangzhen" % e)
	#logging.error("Cannot connect to AWS S3 with Access Key: %s!" % self.access_key)


#bucket = conn.create_bucket('wangz-bucket')

print '========================='
bucket = conn.create_bucket('new-bucket', policy='public-read')
