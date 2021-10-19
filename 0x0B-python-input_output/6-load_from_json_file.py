#!/usr/bin/python3
"""
this reads from a json file and creates an object
"""
import json


def load_from_json_file(filename):
    """
    returns the object
    """
    with open(filename, encoding='utf-8') as filejson:
        return json.load(filejson)
