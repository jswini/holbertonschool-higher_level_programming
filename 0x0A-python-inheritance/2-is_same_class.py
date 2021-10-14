#!/usr/bin/python3
"""
This module checks if an object if of the type passed in
"""
def is_same_class(obj, a_class):
    """
    Here we test the object against the class and return the result
    """
    if type(obj) == a_class:
        return True
    else:
        return False
