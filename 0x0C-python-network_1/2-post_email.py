#!/usr/bin/python3
"""
This module creates a post request with an email to a website
"""

from sys import argv
import urllib.request
import urllib.parse

if __name__ == "__main__":
    email = {'email': argv[2]}
    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req, data) as response:
        new_response = response.read()
    print(new_response)
