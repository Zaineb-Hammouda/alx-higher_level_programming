#!/usr/bin/python3
"""
class square is defined
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class square inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ initializes private attributes """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
    """
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
        returns area value of the rectangle instance
        return self.__height * self.__width

    def display(self):
        prints the rectangle instance with the char "#"
        for i in range(self.y):
            print()
        for j in range(self.height):
            print(" " * self.x + "#" * self.width)
    """

    def to_dictionary(self):
        """ returns a dict representation of a square"""
        return {'id': self.id, 'size': self.width,
                'x': self.x, 'y': self.y}

    def update(self, *args, **kwargs):
        """updates attributes"""
        if args:
            arg = 0
            for i in args:
                if arg == 0:
                    if i is not None:
                        self.id = i
                    else:
                        self.__init__(self.size, self.x, self.y)
                elif arg == 1:
                    self.size = i
                elif arg == 2:
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
                        self.__init__(self.size, self.x, self.y)
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def __str__(self):
        m = "[Square] ({}) {}/{} ".format(self.id, self.x, self.y)
        n = "- {}".format(self.width)
        return m + n
