#!/usr/bin/python3
"""
This module implemets 1 or more steps of the BaseGeometry class
"""


class BaseGeometry:
    """
    This is a starter class for BaseGeometry
    """

    def area(self):
        """
        This is a non implemented area method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method checks if the input is a positive intedge
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):

    """
    this subclass for base geometry creates a rectangle
    """
    def __init__(self, width, height):
        """
        this instantiates the object of the sub class
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
