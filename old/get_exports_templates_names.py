#!/usr/bin/env python
import boto3
import re
import json

inuser = boto3.session.Session(profile_name='inContact-User')

client = inuser.client('cloudformation')

response = client.list_exports()

l = response.get('Exports', {})

for x in l:
    s = x['ExportingStackId']
    print re.search('.*/(.*)/.*', s).group(1),x["Name"]
    t = x["Name"]
    try:
        if client.list_imports(ExportName=t):
            cl = client.list_imports(ExportName=t)
            print json.dumps(cl["Imports"], sort_keys=True, indent=4)
            #print cl["Imports"]
    except:
        pass

    #for r in t:
    #    print client.list_imports(ExportName=r)
