#!/usr/bin/python3
""" the 10-square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square class inherits from Rectangle class"""
    def __init__(self, size):
        """ initializes size attribute"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
