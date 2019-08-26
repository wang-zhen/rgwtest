# -*- coding: utf-8 -*-
import oss2


try:
    auth = oss2.Auth('LTAI7gb42H0riIA7', 'qMvzhm7QQnwlZ7wgKCDxTvSpK2meC6')
    #auth = oss2.Auth('LTAI7gb42H0riIA7', 'qMvzhm7QQnwlZ7wgKCDxTvSpK2meC5')
except Exception,err:
    print err

#bucket = oss2.Bucket(auth, 'http://oss-cn-hangzhou.aliyuncs.com', 'wang-zhen')
#service = oss2.Service(auth, 'http://oss-cn-beijing.aliyuncs.com')
bucket = oss2.Bucket(auth, 'http://oss-cn-beijing.aliyuncs.com', 'wangz-test1')

bucket.create_bucket()
#bucket.create_bucket()
#res = service.list_buckets()
#for bk in res.buckets:
#    print bk.name
#    print bk.creation_date
#    print bk.location
#    print bk.extranet_endpoint
#print([b.name for b in oss2.BucketIterator(service)])
#print bucket
