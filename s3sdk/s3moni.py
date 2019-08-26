#!/usr/bin/env python
#coding=utf8
 
import httplib as http_client
 
httpClient = None


method = "PUT"
path = "/wangz-bucket/"
body = "" 

headers = {'Date': 'Fri, 16 Aug 2019 08:51:30 GMT', 'Content-Length': '0', 'Authorization': u'AWS DI5N4CZDI21SGM7VD5K0:GpbBj5yGkE0EjCpgyt6WK9rajYw=', 'User-Agent': 'Boto/2.49.0 Python/2.7.5 Linux/3.10.0-862.el7.x86_64'}
host = "172.16.103.18"
port = 80

try:
    connection = http_client.HTTPConnection(host, port, timeout=30)
    #connection.request('GET', '/')
    connection.request(method, path, body, headers)
    response = connection.getresponse()
    print response.status
    print response.reason
    print response.getheaders() 
    print response.read()
except Exception, e:
    print e
