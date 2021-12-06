#!/usr/bin/python3
"""
This module takes a URL and displays a value from the header
"""

from sys import argv
import requests

if __name__ == "__main__":
    req = requests.get(argv[1])
    print("{}".format(req.headers['x-request-id']))
