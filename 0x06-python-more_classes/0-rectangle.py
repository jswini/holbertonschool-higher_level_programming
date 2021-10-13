#!/usr/bin/python3
class Rectangle:
    """
    This will define a rectangle object
    """

    def __init__(self, width=0, height=0):
        """
        This instantiates the rectangle
        """
        self.__width = width
        self.__height = height



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
        if value < 0:
            raise ValueError("width must be >= 0")
        if type(value) is not int:
            raise TypeError("width must be an integer")
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
        if value < 0:
            raise ValueError("height must be>= 0")
        elif type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            self.__height = value
