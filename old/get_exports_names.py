#!/usr/bin/env python
import boto3
import json

inuser = boto3.session.Session(profile_name='inContact-User')

s3 = inuser.resource('s3')

client = inuser.client('cloudformation')

response = client.list_exports()

l = response.get('Exports', {})

for x in l:
    print(x["Name"])

