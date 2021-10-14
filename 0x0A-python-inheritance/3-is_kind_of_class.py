#!/usr/bin/python3
"""
this module checks if an object is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """
    we return true or false based on the test
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
