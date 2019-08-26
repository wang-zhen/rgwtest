# -*- coding: utf-8 -*-
import oss2


try:
    auth = oss2.Auth('LTAI7gb42H0riIA7', 'qMvzhm7QQnwlZ7wgKCDxTvSpK2meC6')
    #auth = oss2.Auth('LTAI7gb42H0riIA7', 'qMvzhm7QQnwlZ7wgKCDxTvSpK2meC5')
except Exception,err:
    print err

#bucket = oss2.Bucket(auth, 'http://oss-cn-hangzhou.aliyuncs.com', 'wang-zhen')
#service = oss2.Service(auth, 'http://oss-cn-beijing.aliyuncs.com')
bucket = oss2.Bucket(auth, 'http://oss-cn-beijing.aliyuncs.com', 'wang-zhen')

result = bucket.put_object('wangzhen1', b'wangzhen')
print('http status: {0}'.format(result.status))
print('request_id: {0}'.format(result.request_id))
