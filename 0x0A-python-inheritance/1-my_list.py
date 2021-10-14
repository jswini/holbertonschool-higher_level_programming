#!/usr/bin/python3
"""
This module creates a subclass of list with int data
"""


class MyList(list):
    """
    This instantiates the subclass of super class list
    """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """
        This method sorts the list and then prints it
        """
        new_list = sorted(self)
        return (print(new_list))
