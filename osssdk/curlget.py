# -*- coding: utf-8 -*-

import hmac
import hashlib
import time
import base64
import sys

from email.utils import formatdate

try:
    import simplejson as json
except (ImportError, SyntaxError):
    import json

from urllib import quote as urlquote, unquote as urlunquote
from urlparse import urlparse
import logging

import platform

import requests
from requests.structures import CaseInsensitiveDict

AUTH_VERSION_1 = 'v1'
AUTH_VERSION_2 = 'v2'

logger = logging.getLogger(__name__)


s = requests.Session()
psize = 10
s.mount('http://', requests.adapters.HTTPAdapter(pool_connections=psize, pool_maxsize=psize))
s.mount('https://', requests.adapters.HTTPAdapter(pool_connections=psize, pool_maxsize=psize))

url = 'http://wang-zhen.oss-cn-beijing.aliyuncs.com/wangzhen1'

data = "wangzhen"
#params = {'marker': '', 'prefix': '', 'max-keys': '100'}
params = {}
print("method :", "PUT")
print("url :", url)
print("data :", data)
print("params :", params)
headers = {}
headers = {'date': 'Tue, 20 Aug 2019 04:23:53 GMT', 'Accept-Encoding': None, 'authorization': 'OSS LTAI7gb42H0riIA7:aghlnjzoHsPnxx9i9lmHsRR62Ys=', 'User-Agent': 'aliyun-sdk-python/2.8.0(Linux/3.10.0-862.el7.x86_64/x86_64;2.7.5)'}
print("headers :", headers)

response = s.request('PUT', url,data=data,params=params,headers=headers,stream=True,timeout=60)
print "111111111"
print response.status_code
print response.headers
print response.headers.get('x-aws-request-id', '')

_CHUNK_SIZE = 8 * 1024

for chunk in response.iter_content(_CHUNK_SIZE):
    print chunk
