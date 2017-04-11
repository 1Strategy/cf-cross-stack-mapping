#!/usr/bin/env python
import boto3
import re

inuser = boto3.session.Session(profile_name='inContact-User')

client = inuser.client('cloudformation')

response = client.list_exports()

l = response.get('Exports', {})

print "Templates."
for x in l:
    s = x['ExportingStackId']
    print "Templates.",re.search('.*/(.*)/.*', s).group(1),'.',x['Name']
    name1 = "Templates.",re.search('.*/(.*)/.*', s).group(1),'.',x['Name']
    t = x["Name"]
    # for z in t:
    #     if client.list_imports(ExportName=t):
    #         cl = client.list_imports(ExportName=t)
    #         print cl["Imports"]
    #         print name1,'.'.join(cl["Imports"])
    #print "Templates.",re.search('.*/(.*)/.*', s).group(1),'.',x["Name"],'.'

    #print(re.search('.*/(.*)/.*', s).group(1),".",x["Name"],".",sep='',end='')
    #print "Templates.",'.'.join([re.search('.*/(.*)/.*', s).group(1),x["Name"]]) + '.'
    #print "Templates.",re.search('.*/(.*)/.*', s).group(1),x["Name"] + '.',
    #t = x["Name"]
    #try:
    #    if client.list_imports(ExportName=t):
    #        cl = client.list_imports(ExportName=t)
    #        #print cl["Imports"]
    #        #print '.'.join(cl["Imports"])
    #        print '.'.join([re.search('.*/(.*)/.*', s).group(1),x["Name"]]) + '.','.'.join(cl["Imports"])
    #except:
    #    print '.',
    #    pass
