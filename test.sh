#!/bin/bash -x  
set -v
bucket="wang-zhen" 
dateValue=`date` 
resource="/${bucket}/" 
contentType="application/octet-stream" 
stringToSign="PUT\n\n\n${dateValue}\n${resource}" 
s3Key="LTAI7gb42H0riIA7" 
s3Secret="qMvzhm7QQnwlZ7wgKCDxTvSpK2meC5" 
signature=`echo -en ${stringToSign} | openssl sha1 -hmac ${s3Secret} -binary | base64` 
curl -v -X GET "http://oss-cn-beijing.aliyuncs.com" -H "Host: oss-cn-beijing.aliyuncs.com" -H "Date: ${dateValue}" -H "Authorization: OSS ${s3Key}:${signature}"
