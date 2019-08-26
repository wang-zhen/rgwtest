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

#url = 'http://172.16.103.18/wangz-bucket/?max-keys=100'
#url = 'http://172.16.103.18/wangz-bucket234/'
url = 'http://172.16.103.56:5000/v1/storage/oss/wangz-bucket/wangz'

data = 'wangzhen'
#params = {'marker': '', 'prefix': '', 'max-keys': '100'}
params = {}
print("method :", "PUT")
print("url :", url)
print("data :", data)
print("params :", params)
headers = {}
headers = {'Content-Length': '8', 'Content-MD5': 'Lt0CMx0D0xbYVaVgxH159g==', 'Expect': '100-Continue', 'Date': 'Wed, 21 Aug 2019 08:04:24 GMT', 'User-Agent': 'Boto/2.49.0 Python/2.7.5 Linux/3.10.0-862.el7.x86_64', 'Content-Type': 'application/octet-stream', 'Authorization': u'AWS DI5N4CZDI21SGM7VD5K0:nSAQ768G7xqSnMOlj8HzLrkCSyE='}

#headers['Accept'] = '*/*'
#headers['User-Agent'] = 'curl/7.29.0'
#headers['Accept-Encoding'] = None
#headers['Date'] = 'Mon, 19 Aug 2019 05:02:29 GMT'
#headers['Authorization'] = 'AWS DI5N4CZDI21SGM7VD5K0:7urX7/lM02Ug5XZLd9CHHDVCCkU='
print("headers :", headers)

response = s.request('PUT', url,data=data,params=params,headers=headers,stream=True,timeout=60)
print "111111111"
print response.status_code
print response.headers
print response.headers.get('x-aws-request-id', '')

_CHUNK_SIZE = 8 * 1024

for chunk in response.iter_content(_CHUNK_SIZE):
    print chunk
