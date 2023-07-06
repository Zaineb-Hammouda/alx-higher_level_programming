#!/usr/bin/python3
""" class Rectangle that defines a rectangle"""


class Rectangle:
    """ defines a ractangle """
    def __init__(self, width=0, height=0):
        """ instantiation with width and height"""
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """getter method to retrieve the height"""
        return self.__height

    @property
    def width(self):
        """ getter to retrieve the width attribute"""
        return self.__width

    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")

    @width.setter
    def width(self, value):
        """setter that changes value of width"""
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
