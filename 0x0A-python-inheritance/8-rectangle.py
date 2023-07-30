#!/usr/bin/python3
""" the 8-rectangle module"""


class Rectangle(BaseGeometry):
    """ Rectangle class inherits from BaseGeometry class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
