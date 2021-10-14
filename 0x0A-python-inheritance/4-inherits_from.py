#!/usr/bin/python3
"""
this module tests if an object is of a type that is a subclass of the
passed info
"""


def inherits_from(obj, a_class):
    """
    we return true or false based on the test
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
