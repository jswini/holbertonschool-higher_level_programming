#!/usr/bin/python3
"""
this module reads from a file and outputs result to the screen
"""
def read_file(filename=""):
    """
    """
    with open("my_file_0.txt", encoding='utf-8') as my_read_file:
        print(my_read_file.read(), end="")
