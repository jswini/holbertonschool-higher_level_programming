#!/usr/bin/python3
"""
This module creates a URL request to a website and displays errors
"""

from sys import argv
import requests

if __name__ == "__main__":
    req = requests.get(argv[1])
    if req.status_code == 200:
        print("{}".format(req.text))
    else:
        print("Error Code: {}".format(req.status_code))
