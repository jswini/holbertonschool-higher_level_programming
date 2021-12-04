#!/usr/bin/python3
import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    urllib.response.addinfourl
print("type: {}".format(type(html)))
print("content: {}".format(html))
print("utf8 content: {}".format(html.decode('utf-8')))
