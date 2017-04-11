#!/usr/bin/env python
import boto3
import re

inuser = boto3.session.Session(profile_name='inContact-User')

s3 = inuser.resource('s3')

client = inuser.client('cloudformation')

response = client.list_exports()

l = response.get('Exports', {})

for x in l:
    s = x['ExportingStackId']
    #p = re.compile('.*/(.*)/.*')
    print re.search('.*/(.*)/.*', s).group(1)
    #print p.findall(s)
    #print p.match(s).groups()
    #print(x['ExportingStackId'])

