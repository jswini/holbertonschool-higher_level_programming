#!/usr/bin/python3
import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    urllib.response.addinfourl
print(response.headers.get("X-Request-Id"))
