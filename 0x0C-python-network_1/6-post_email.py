#!/usr/bin/python3
"""
This module creates a post request with an email to a website
"""

from sys import argv
import requests

if __name__ == "__main__":
    email = {'email': argv[2]}
    req = requests.post(argv[1], email)
    print("{}".format(req.text))
