#!/usr/bin/python3
"""
This will define a rectangle object
"""


class Rectangle:
    """
    This instantiates the rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        This returns the width property of our rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This sets the width of the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        This returns the height property of our rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This sets the height of the rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        This module sets the area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        This module sets the perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """
        prints the rectangle using # to show the dimensions
        """
        pound = "#"
        rectangleString = ""
        if self.width == 0 or self.height == 0:
            return ("")
        else:
            for i in range(self.height):
                for j in range(self.width):
                    rectangleString += pound
                if i < self.height - 1:
                    rectangleString += "\n"
        return rectangleString

    def __repr__(self):
        """
        returns the rectangle using # to show the dimensions
        """
        pound = "#"
        rectangleString = ""
        if self.width == 0 or self.height == 0:
            return ("")
        else:
            return ("Rectangle({}, {})".format(self.width, self.height))
