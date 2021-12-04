#!/usr/bin/python3
'''
This sends a request to url and manages errors
'''
from sys import argv
from urllib import request, parse, error
if __name__ == "__main__":
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as response:
            new_response = response.read()
        print("{}".format(new_response.decode()))
    except error.HTTPError as err_type:
        print(err_type.code)
