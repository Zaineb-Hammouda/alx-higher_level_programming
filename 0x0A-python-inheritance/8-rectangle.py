#!/usr/bin/python3
""" the 8-rectangle module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class inherits from BaseGeometry class"""
    def __init__(self, width, height):
        """ initializes heigth and width attributes"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
