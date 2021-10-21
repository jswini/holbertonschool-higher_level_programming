#!/usr/bin/python3
"""
"""


class Base:
    """
    This is the base class for almost a circle
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        This method instantiates an object of class base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
