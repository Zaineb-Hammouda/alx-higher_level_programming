#!/usr/bin/python3
"""
the base module
defines a class Base
"""
import json
import os
import os.path
import csv
import turtle


class Base:
    """
    defines a class instance base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializes public instance attributes
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string rep of list_dictionnaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string rep of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dicts = []
                for i in list_objs:
                    dicts.append(i.to_dictionary())
                f.write(Base.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the Json string rep json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attrs set"""
        if dictionary:
            if cls.__name__ == "Rectangle":
                rectangle = cls(6, 5)
            else:
                rectangle = cls(6)
            rectangle.update(**dictionary)
            return rectangle

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances"""
        filename = cls.__name__ + ".json"
        if os.path.isfile(filename) is True:
            with open(filename, "r", encoding="utf-8") as f:
                read = f.read()
                jlist = Base.from_json_string(read)
                ilist = []
                for i in jlist:
                    instance = cls.create(**i)
                    ilist.append(instance)
                return ilist
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes in csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as f:
            if list_objs is None:
                f.write("[]")
            else:
                if cls.__name__ == "Square":
                    csv_format = ["id", "size", "x", "y"]
                elif cls.__name__ == "Rectangle":
                    csv_format = ["id", "width", "height", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=csv_format)
                for i in list_objs:
                    writer.writerow(i.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """deserializes a csv file"""
        filename = cls.__name__ + ".csv"
        if os.path.isfile(filename) is True:
            with open(filename, "r", newline="") as f:
                if cls.__name__ == "Square":
                    csv_format = ["id", "size", "x", "y"]
                elif cls.__name__ == "Rectangle":
                    csv_format = ["id", "width", "height", "x", "y"]

                ldct = csv.DictReader(f, fieldnames=csv_format)
                ldct = [dict([k, int(v)] for k, v in d.items()) for d in ldct]
                return [cls.create(**d) for d in ldct]
        else:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""
        """create turtle object"""
        t = turtle.Turtle()
        """choose the pensize, shape of the character you will draw with,
        it's color and the background color of the screen/window"""
        t.shape("turtle")
        t.color("lightgreen")
        t.pensize(4)
        t.screen.bgcolor("#90EE90")

        """loop over each list and for each obj:
        move the turtle up and down to skip x and y"""
        for square in list_squares:
            t.showturtle()
            t.up()
            t.goto(square.x, square.y)
            t.down()
            """ move turtle to draw width/size of the square"""
            for i in range(2):
                for j in range(2):
                    t.forward(square.width)
                    t.left(90)
            t.hideturtle()

        for rectangle in list_rectangles:
            t.showturtle()
            t.up()
            t.goto(square.x, square.y)
            t.down()
            for i in range(2):
                t.forward(rectangle.width)
                t.left(90)
                t.forward(rectangle.height)
                t.left(90)
            t.hideturtle()

        t.exitonclick()
