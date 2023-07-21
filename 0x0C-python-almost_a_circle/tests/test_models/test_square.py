#!/usr/bin/python3
"""
unittest model
Unittest for Square()
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import io
import sys


class TestSquare(unittest.TestCase):
    """
    unittest class to test the Square class
    """
    def test_0_args(self):
        """test for no arguments"""
        with self.assertRaises(TypeError):
            print(Square())

    def test_1_arg(self):
        s1 = Square(1)
        self.assertEqual(1, s1.size)

    def test_2_args(self):
        s1 = Square(1, 2)
        self.assertEqual((1, 2), (s1.size, s1.x))

    def test_3_args(self):
        s1 = Square(1, 2, 3)
        self.assertEqual((1, 2, 3), (s1.size, s1.x, s1.y))

    def test_str_size(self):
        with self.assertRaises(TypeError):
            print(Square("1"))

    def test_str_x(self):
        with self.assertRaises(TypeError):
            print(Square(1, "2"))

    def test_str_y(self):
        with self.assertRaises(TypeError):
            print(Square(1, 2, "3"))

    def test_4_args(self):
        s1 = Square(1, 2, 3, 4)
        self.assertEqual((1, 2, 3, 4), (s1.size, s1.x, s1.y, s1.id))

    def test_negative_size(self):
        with self.assertRaises(ValueError):
            print(Square(-1))

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            print(Square(1, -2))

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            print(Square(1, 2, -3))

    def test_zero_size(self):
        with self.assertRaises(ValueError):
            print(Square(0))

    def test__str__(self):
        s1 = Square(4, 6, 2, 1)
        self.assertEqual("[Square] (1) 6/2 - 4", s1.__str__())

class test_display(unittest.TestCase):
    @staticmethod
    def stdout_return(instance, method):
        out = io.StringIO()
        sys.stdout = out
        if method == "display":
            instance.display()
        elif method == "print":
            print(instance)
        else:
            instance.to_dictionary()
        sys.stdout = sys.__stdout__
        return out

    def test_no_XY(self):
        s1 = Square(2)
        m = test_display.stdout_return(s1, "display")
        sqr = "##\n##\n"
        self.assertEqual(sqr, m.getvalue())

    def test_all(self):
        s1 = Rectangle(2, 1, 1)
        m = test_display.stdout_return(s1, "display")
        sqr = " ##\n"
        self.assertEqual(sqr, m.getvalue())

class test_to_dict(unittest.TestCase):
    """unittest class for to_dictionary method"""
    def test_dict_all(self):
        s1 = Square(10, 2, 1)
        s1_dict = s1.to_dictionary()
        self.assertEqual(str(s1_dict), str(s1.to_dictionary()))

class test_update(unittest.TestCase):
    """unittest class for the update method"""
    @staticmethod
    def stdout_return(instance, method):
        out = io.StringIO()
        sys.stdout = out
        if method == "display":
            instance.display()
        else:
            print(instance)
        sys.stdout = sys.__stdout__
        return out

    def test_no_args(self):
        s1 = Square(10, 10, 10)
        s1.update()
        m = test_update.stdout_return(s1, "print")
        self.assertEqual(m.getvalue(), s1.__str__() + '\n')

    def test_one_arg(self):
        r1 = Square(10, 10, 10)
        r1.update(89)
        m = test_update.stdout_return(r1, "print")
        self.assertEqual(m.getvalue(), r1.__str__() + '\n')

    def test_two_args(self):
        r1 = Square(10, 10, 10)
        r1.update(89, 2)
        m = test_update.stdout_return(r1, "print")
        self.assertEqual(m.getvalue(), r1.__str__() + '\n')

    def test_3_args(self):
        r1 = Square(10, 10, 10)
        r1.update(89, 2, 3)
        m = test_update.stdout_return(r1, "print")
        self.assertEqual(m.getvalue(), r1.__str__() + '\n')

    def test_4_args(self):
        r1 = Square(10, 10, 10)
        r1.update(89, 2, 3, 4)
        m = test_update.stdout_return(r1, "print")
        self.assertEqual(m.getvalue(), r1.__str__() + '\n')

    def test_kwargs_size(self):
        r1 = Square(10, 10, 10)
        r1.update(size=1)
        m = test_update.stdout_return(r1, "print")
        self.assertEqual(m.getvalue(), r1.__str__() + '\n')

    def test_kwargs_id(self):
        r1 = Square(10, 10, 10)
        r1.update(id=98)
        m = test_update.stdout_return(r1, "print")
        self.assertEqual(m.getvalue(), r1.__str__() + '\n')

    def test_kwargs_2args(self):
        r1 = Square(10, 10, 10)
        r1.update(y=1, x=2)
        m = test_update.stdout_return(r1, "print")
        self.assertEqual(m.getvalue(), r1.__str__() + '\n')

    def test_kwargs_3args(self):
        r1 = Square(10, 10, 10)
        r1.update(y=1, size=2, x=3)
        m = test_update.stdout_return(r1, "print")
        self.assertEqual(m.getvalue(), r1.__str__() + '\n')

    def test_kwargs_4args(self):
        r1 = Square(10, 10, 10)
        r1.update(y=1, size=2, x=3, id=89)
        m = test_update.stdout_return(r1, "print")
        self.assertEqual(m.getvalue(), r1.__str__() + '\n')

class test_create_method(unittest.TestCase):
    """unittest for the create method"""
    def test_creates_instance(self):
        r1 = Square(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertEqual(type(r1), type(r2))

class test_save_load_file(unittest.TestCase):
    """unittest for the save_to_file method"""
    def test_empty_list(self):
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual("[]", f.read())

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_none(self):
        Square.save_to_file(None)
        with open("Square.json") as f:
            self.assertEqual("[]", f.read())

    def test_one_obj(self):
        Square.save_to_file([Square(1)])
        m = '[{"id": 46, "size": 1, "x": 0, "y": 0}]'
        with open("Square.json") as f:
            self.assertEqual(m, f.read())

    def test_file_no_exist(self):
        out = Square.load_from_file()
        self.assertEqual([], out)

    def test_load_file_exists(self):
        r1 = Square(10, 7, 2, 1)
        Square.save_to_file([r1])
        out = Square.load_from_file()
        self.assertEqual(str(r1), str(out[0]))

if __name__ == "__main__":
    unittest.main()
