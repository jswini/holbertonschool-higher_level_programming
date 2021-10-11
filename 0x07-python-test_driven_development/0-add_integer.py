#!/usr/bin/python3
"""
This module checks if the inputs are ints and if so adds them.

If the inputs are not ints an error will be thrown.

    Typical usage example:

    add_integer(a, b)
"""


def add_integer(a, b=98):
    """
    Function to add the ints

    Args:
        a: first int to add
        b: second int to add

    Returns:
        The sum of the 2 ints

    Raises:
        Exeption: if either input is not an int
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if isinstance(a, int):
        if isinstance(b, int):
            return a+b
        else:
            return ("b must be an integer")
    else:
        return ("a must be an integer")
