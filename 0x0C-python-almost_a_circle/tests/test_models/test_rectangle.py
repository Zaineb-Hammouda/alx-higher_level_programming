#!/usr/bin/python3
"""
unittest model
Unittest for Rectangle()
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import io
import sys


class TestRectangle(unittest.TestCase):
    """
    unittest class to test the Rectangle class
    """
    def test_0_args(self):
        """test for no arguments"""
        with self.assertRaises(TypeError):
            print(Rectangle())

    def test_2_args(self):
        r1 = Rectangle(1, 2)
        self.assertEqual((1, 2), (r1.width, r1.height))

    def test_3_args(self):
        r1 = Rectangle(1, 2, 3)
        self.assertEqual((1, 2, 3), (r1.width, r1.height, r1.x))

    def test_4_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        self.assertEqual((1, 2, 3, 4), (r1.width, r1.height, r1.x, r1.y))

    def test_str_width(self):
        with self.assertRaises(TypeError):
            print(Rectangle("1", 2))

    def test_str_height(self):
        with self.assertRaises(TypeError):
            print(Rectangle(1, "2"))

    def test_str_x(self):
        with self.assertRaises(TypeError):
            print(Rectangle(1, 2, "3"))

    def test_str_y(self):
        with self.assertRaises(TypeError):
            print(Rectangle(1, 2, 3, "4"))

    def test_5_args(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual((1, 2, 3, 4, 5), (r1.width, r1.height, r1.x, r1.y, r1.id))

    def test_negative_w(self):
        with self.assertRaises(ValueError):
            print(Rectangle(-1, 2))

    def test_negative_h(self):
        with self.assertRaises(ValueError):
            print(Rectangle(1, -2))

    def test_zero_w(self):
        with self.assertRaises(ValueError):
            print(Rectangle(0, 2))

    def test_zero_h(self):
        with self.assertRaises(ValueError):
            print(Rectangle(1, 0))

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            print(Rectangle(1, 2, -3))

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            print(Rectangle(1, 2, 3, -4))

    def test_area(self):
        r1 = Rectangle(2, 4)
        self.assertEqual(8, r1.area())

    def test__str__(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual("[Rectangle] (12) 2/1 - 4/6", r1.__str__())

class test_display(unittest.TestCase):
    """unittest class to test to_json_string method"""
    @staticmethod
    def stdout_return(instance, method):
        out = io.StringIO()
        sys.stdout = out
        instance.display()
        sys.stdout = sys.__stdout__
        return out

    def test_no_XY(self):
        r1 = Rectangle(2, 2)
        m = test_display.stdout_return(r1, "display")
        rect = "##\n##\n"
        self.assertEqual(rect, m.getvalue())

    def test_with_x(self):
        r1 = Rectangle(2, 2, 1)
        m = test_display.stdout_return(r1, "display")
        rect = " ##\n ##\n"
        self.assertEqual(rect, m.getvalue())

    def test_all(self):
        r1 = Rectangle(2, 2, 1, 1)
        m = test_display.stdout_return(r1, "display")
        rect = "\n ##\n ##\n"
        self.assertEqual(rect, m.getvalue())

class test_to_dict(unittest.TestCase):
    """unittest class for to_dictionary method"""
    def test_dict_all(self):
        r1 = Rectangle(10, 2, 1, 9)
        r1_dict = {'id': 15, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r1_dict, r1.to_dictionary())

    def test_dict_noXY(self):
        r1 = Rectangle(10, 2)
        r1_dict = {'id': 16, 'width': 10, 'height': 2, 'x': 0, 'y': 0}
        self.assertEqual(r1_dict, r1.to_dictionary())

class test_update(unittest.TestCase):
    """unittest class for the update method"""
"""
    def test_empty_string(self):
        output = Rectangle.from_json_string("[]")
        self.assertEqual([], output)

    def test_None_input(self):
        output = Rectangle.from_json_string(None)
        self.assertEqual([], output)

    def test_return_list(self):
        j_list = Base.from_json_string('[{"id": 12}]')
        self.assertEqual([{'id': 12}], j_list)
        """
