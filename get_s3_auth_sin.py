from email.utils import formatdate


class provider(object):
     def __init__(self, date_header=None, ):
         self.date_header = 'x-amz-date'
         self.header_prefix = 'x-amz-'

headers = {'User-Agent': 'Boto/2.49.0 Python/2.7.5 Linux/3.10.0-862.el7.x86_64'}
method = 'GET'
auth_path = '/'
headers['Date'] = formatdate(usegmt=True)

#string_to_sign = boto.utils.canonical_string(method, auth_path,headers, None,self._provider)

print headers
