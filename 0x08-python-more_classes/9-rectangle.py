#!/usr/bin/python3
""" class Rectangle that defines a rectangle"""


class Rectangle:
    """ defines a ractangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ instantiation with width and height"""
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ getter to retrieve the width attribute"""
        return self.__width

    @property
    def height(self):
        """getter method to retrieve the height"""
        return self.__height

    @width.setter
    def width(self, value):
        """setter that changes value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """ setter for the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ calculates the area of the rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ calculates the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __str__(self):
        """ depicts data as string"""
        rect = []
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    rect.append("#")
                rect.append("\n")
            rect.pop()
        return "".join(rect)

    def __repr(self):
        """returns string representation of our rectangle"""
        return "Rectangle({:d}, {:d}".format(self.__width, self.__height)

    def __del__(self):
        """deletes object of a class and prints a message"""
        Rectangle.number_of_instances -= 1
        print("{:s}".format("Bye rectangle..."))

    @classmethod
    def square(cls, size=0):
        instance = cls()
        instance.width = size
        instance.height = size
        return instance
