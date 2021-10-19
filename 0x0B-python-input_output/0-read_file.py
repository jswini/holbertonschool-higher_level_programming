#!/usr/bin/python3
"""
this module reads from a file and outputs result to the screen
"""


def read_file(filename=""):
    """
    open read and print the file
    """
    with open(filename, encoding='utf-8') as my_read_file:
        print(my_read_file.read(), end="")
