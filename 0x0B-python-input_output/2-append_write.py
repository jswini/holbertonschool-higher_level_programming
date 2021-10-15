#!/usr/bin/python3
"""
this module append to a file
"""


def append_write(filename="", text=""):
    """
    we open the file, append, then reopen to read and output
    """
    with open(filename, mode='a', encoding='utf-8') as appended_file:
        appended_file.write(text)
    with open(filename, encoding='utf-8') as appended_file:
        length = appended_file.read()
    return (len(length))
