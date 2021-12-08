#!/usr/bin/python3
'''
This script searches for a dict and displays as json if there
'''
import requests
from sys import argv

if __name__ == "__main__":
    
    if len(argv) > 1:
        search_term = argv[1]
    else:
        search_term = ""
    try:
        req = requests.post('http://0.0.0.0:5000/search_user', data = {'q': search_term})
        reqjson = req.json()
        req.raise_for_status()
        print("[{}] {}".format(reqjson["id"], reqjson["name"], end=""))
    except ValueError as jsonerror:
        print("Not a valid JSON")
    except:
        print("No result")
        pass
    
