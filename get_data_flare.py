#!/usr/bin/env python
import boto3
import re

inuser = boto3.session.Session(profile_name='default')
client = inuser.client('cloudformation')
response = client.list_exports()
f1=open('temp.in', 'w+')
l = response.get('Exports', {})
print >>f1, 'id,value'
print >>f1, 'Templates,'
for x in l:
    s = x['ExportingStackId']
    t = x["Name"]
    print >>f1, '.'.join(['Templates',re.search('.*/(.*)/.*', s).group(1),t]) + ','
    j = re.search('.*/(.*)/.*', s).group(1)
    print >>f1, '.'.join(['Templates',j]) + ','
    try:
        if client.list_imports(ExportName=t):
            cl = client.list_imports(ExportName=t)
            im = cl["Imports"]
            for x in im:
                print >>f1, '.'.join(['Templates',j,t,x]) + ','
    except:
        pass
#for x in l:
#    s = x['ExportingStackId']
#    print '.'.join(['Templates',re.search('.*/(.*)/.*', s).group(1)]) + ','
f1.close()

lines_seen = set()
outfile = open('flare.csv', "w")
for line in open('temp.in', "r"):
   if line not in lines_seen: # not a duplicate
       outfile.write(line)
       lines_seen.add(line)
outfile.close()
