#!/usr/bin/python3
"""
class Rectangle is defined
"""
from models.base import Base


class Rectangle(Base):
    """
    class rectangle inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializes private attributes """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns area value of the rectangle instance"""
        return self.__height * self.__width

    def display(self):
        """ prints the rectangle instance with the char "#" """
        for i in range(self.y):
            print()
        for j in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """ updates attributes """
        if args:
            arg = 0
            for i in args:
                if arg == 0:
                    if i is not None:
                        self.id = i
                    else:
                        self.__init__(self.width, self.height, self.x, self.y)
                elif arg == 1:
                    self.width = i
                elif arg == 2:
                    self.height = i
                elif arg == 3:
                    self.x = i
                else:
                    self.y = i
                arg += 1
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    if value is not None:
                        self.id = value
                    else:
                        self.__init__(self.width, self.height, self.x, self.y)
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def __str__(self):
        m = "[Rectangle] ({}) {}/{} ".format(self.id, self.x, self.y)
        n = "- {}/{}".format(self.width, self.height)
        return m + n
