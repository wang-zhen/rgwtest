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

print('0000000000000000000000000000000000000000000')
bucket.put_object_from_file('wangzhen1', 'local-50M-file')


#with open('local-50M-file', 'rb') as fileobj:
    #fileobj.seek(, os.SEEK_SET)
    #current = fileobj.tell()
#    bucket.put_object('wangzhen1', fileobj)
