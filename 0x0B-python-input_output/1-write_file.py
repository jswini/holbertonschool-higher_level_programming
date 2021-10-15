#!/usr/bin/python3
"""
This module writes files
"""


def write_file(filename="", text=""):
    """
    here we open the file, write to it, then reopen to display it
    """
    with open(filename, mode="w", encoding='utf-8') as new_file:
        new_file.write(text)
    with open(filename, encoding='utf-8') as read_file:
        chars = read_file.read()
        return (len(chars))
