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
	#logging.error("wangzhen" % e)
	#logging.error("Cannot connect to AWS S3 with Access Key: %s!" % self.access_key)


bucket = conn.delete_bucket('wangz-bucket234')

#res = conn.get_all_buckets()
print("ennnnnnnnnnnnnnnd")
#print(res)
sys.exit(0)

#for bucket in conn.get_all_buckets():
#    print "{name}".format(
#        name = bucket.name,
#        reated = bucket.creation_date,
#        )


bucket = conn.get_bucket('test4')
print bucket.name

key = bucket.new_key('dir2/')
#key.set_contents_from_filename('./wenben.txt')
#key.set_contents_from_string('Hello World!')

for key in bucket.list():
        print "{name}\t{size}\t{modified}".format(
                name = key.name,
                size = key.size,
                modified = key.last_modified,
              )

key1 = bucket.get_key('test.py')
key1.set_canned_acl('public-read')
key1 = bucket.get_key('tupian.jpg')
key1.set_canned_acl('public-read')
key1 = bucket.get_key('wenben.txt')
key1.set_canned_acl('public-read')
#key1.get_contents_to_filename('test.py')


#py_key = bucket.new_key('test.py')
#py_key.set_contents_from_filename('./test.py')

hello_key = bucket.get_key('tupian.jpg')
hello_url = hello_key.generate_url(3600, query_auth=False, force_http=True)
plans_url = hello_key.generate_url(3600, query_auth=True, force_http=True)
print hello_url
print plans_url

hello_key = bucket.get_key('wenben.txt')
hello_url = hello_key.generate_url(3600, query_auth=False, force_http=True)
plans_url = hello_key.generate_url(3600, query_auth=True, force_http=True)
print hello_url
print plans_url
