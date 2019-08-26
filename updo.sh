#!/bin/bash -x
set -v
host=oss-cn-beijing.aliyuncs.com
bucket=wangzhen1
Id=LTAI7gb42H0riIA7
Key=qMvzhm7QQnwlZ7wgKCDxTvSpK2meC6
method=$1
source=$2
dest=$3
if test -z "$method"
then
    method=GET
fi
if [ "get" = ${method} ] || [ "GET" = ${method} ]
then
    method=GET
elif [ "put" = ${method} ] || [ "PUT" = ${method} ]
then
    method=PUT
else
    method=GET
fi
if test -z "$dest"
then
    dest=$source
fi
if test -z "$method" || test -z "$source" || test -z "$dest"
then
    echo $0 put localfile objectname
    echo $0 get objectname localfile
    exit -1
fi
if [ "put" = ${method} ] || [ "PUT" = ${method} ]
then
    resource="/${bucket}/${dest}"
    contentType=`file -ib ${source} |awk -F ";" '{print $1}'`
    dateValue="`TZ=GMT date +'%a, %d %b %Y %H:%M:%S GMT'`"
    stringToSign="${method}\n\n${contentType}\n${dateValue}\n${resource}"
    signature=`echo -en ${stringToSign} | openssl sha1 -hmac ${Key} -binary | base64`
    url=http://${host}/${resource}
    echo "upload ${source} to ${url}"
    curl -i -q -X PUT -T "${source}" \
      -H "Host: ${host}" \
      -H "Date: ${dateValue}" \
      -H "Content-Type: ${contentType}" \
      -H "Authorization: OSS ${Id}:${signature}" \
      ${url}
else
    resource="/${bucket}/${source}"
    contentType=""
    dateValue="`TZ=GMT date +'%a, %d %b %Y %H:%M:%S GMT'`"
    stringToSign="${method}\n\n${contentType}\n${dateValue}\n${resource}"
    signature=`echo -en ${stringToSign} | openssl sha1 -hmac ${Key} -binary | base64`
    url=http://${host}/${resource}
    echo "download ${url} to ${dest}"
    curl --create-dirs \
      -H "Host: ${host}" \
      -H "Date: ${dateValue}" \
      -H "Content-Type: ${contentType}" \
      -H "Authorization: OSS ${Id}:${signature}" \
      ${url} -o ${dest}
fi
