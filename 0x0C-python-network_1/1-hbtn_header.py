#!/usr/bin/python3
import sys
import urllib.request
with urllib.request.urlopen(sys.argv[1]) as response:
    html = response.read()
    urllib.response.addinfourl
print(response.headers.get("X-Request-Id"))
