#!/usr/bin/python3
import json
"""
write json data to a file
"""


def save_to_json_file(my_obj, filename):
    """
    does the writing
    """
    with open(filename, mode='w', encoding='utf=8') as filename:
        json.dump(my_obj, filename)
