#!/usr/bin/python3
'''
This module gets the x request id from a website taken in as an arg
'''
import sys
import urllib.request
with urllib.request.urlopen(sys.argv[1]) as response:
    html = response.read()
    urllib.response.addinfourl
print(response.headers.get("X-Request-Id"))
