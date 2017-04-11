#!/usr/bin/env python
import boto3
import json

inuser = boto3.session.Session(profile_name='inContact-User')

s3 = inuser.resource('s3')

#for bucket in s3.buckets.all():
#    print(bucket.name)

client = inuser.client('cloudformation')

#response = client.list_exports(
#    NextToken='string'
#)

response = client.list_exports()
#print(response)
#print json.dumps(response, sort_keys=True, indent=4)
#print(response["Exports"][0]["Name"])
#print(response["NextToken"][0])

#print(response.values()[0][0]["Name"])

#print(response.get('Exports', {}))
l = response.get('Exports', {})
#print '\n'.join(str(p) for p in l) 

for x in l:
    #print(x["Name"])
    print x["Name"],"|",x["Value"]

#for i in response:
#    print response[i]

