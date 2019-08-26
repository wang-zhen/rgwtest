# -*- coding: utf-8 -*-
import os
from oss2 import SizedFileAdapter, determine_part_size
from oss2.models import PartInfo
import oss2

try:
    auth = oss2.Auth('LTAI7gb42H0riIA7', 'qMvzhm7QQnwlZ7wgKCDxTvSpK2meC6')
    #auth = oss2.Auth('LTAI7gb42H0riIA7', 'qMvzhm7QQnwlZ7wgKCDxTvSpK2meC5')
except Exception,err:
    print err

bucket = oss2.Bucket(auth, 'http://oss-cn-beijing.aliyuncs.com', 'wang-zhen')

key = 'wangzhen1'
filename = './local-50M-file'

total_size = os.path.getsize(filename)
part_size = determine_part_size(total_size, preferred_size=100 * 1024)
parts = []

print("total_size:", total_size)
print("part_size:", part_size)

upload_id = bucket.init_multipart_upload(key).upload_id

with open(filename, 'rb') as fileobj:
    part_number = 1
    offset = 0
    while offset < total_size:
        num_to_upload = min(part_size, total_size - offset)
        result = bucket.upload_part(key, upload_id, part_number,SizedFileAdapter(fileobj, num_to_upload))

        parts.append(PartInfo(part_number, result.etag))
        offset += num_to_upload
        part_number += 1

print('0000000000000000000000000000000000000000000')
