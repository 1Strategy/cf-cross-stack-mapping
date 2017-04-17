#!/usr/bin/env python
import boto3
import re

f1=open('sourcedata-output.json', 'w+')
inuser = boto3.session.Session(profile_name='default')
client = inuser.client('cloudformation')
response = client.list_exports()
l = response.get('Exports', {})
print >>f1, '{ "links": ['
output1 = []
for x in l:
    s = x['ExportingStackId']
    t = x["Name"]
    o1 = str('{"source":"' + re.search('.*/(.*)/.*', s).group(1) + '","target":"' + t + '","value":"1.0"}')
    output1.append(o1)
    try:
        if client.list_imports(ExportName=t):
            cl = client.list_imports(ExportName=t)
            im = cl["Imports"]
            for x in im:
                o2 = str('{"source":"' + t + '","target":"' + x + '","value":"1.0"}')
                output1.append(o2)
    except:
        pass
print >>f1, ",\n".join(output1)
print >>f1, '], "nodes": ['
output2 = []
for x in l:
    s = x['ExportingStackId']
    o1 = str('{"name":"' + re.search('.*/(.*)/.*', s).group(1) + '"}')
    output2.append(o1)
for x in l:
    o2 = str('{"name":"' + x["Name"] + '"}')
    output2.append(o2)
    t = x["Name"]
    try:
        if client.list_imports(ExportName=t):
            cl = client.list_imports(ExportName=t)
            im = cl["Imports"]
            for z in im:
                o3 = str('{"name":"' + z + '"}')
                output2.append(o3)
    except:
        pass
print >>f1, ",\n".join(list(set(output2)))
print >>f1, ']}'
f1.close()
