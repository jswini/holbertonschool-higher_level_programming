#!/usr/bin/python3
"""
this module creates a square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class is a sub class of rectangle for a square
    """

    def __init__(self, size):
        """
        this method sets up a square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        this gets the area of the square
        """
        return (self.__size ** 2)

    def __str__(self):
        """
        prints the dimensions as[Square] <width>/<height>
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))
