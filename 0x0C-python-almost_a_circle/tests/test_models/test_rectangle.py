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
        if method == "display":
            instance.display()
        elif method == "print":
            print(instance)
        else:
            instance.to_dictionary()
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
        r1_dict = r1.to_dictionary()
        self.assertEqual(str(r1_dict), str(r1.to_dictionary()))

    def test_dict_noXY(self):
        r1 = Rectangle(10, 2)
        r1_dict = {'id': 20, 'width': 10, 'height': 2, 'x': 0, 'y': 0}
        self.assertDictEqual(r1_dict, r1.to_dictionary())

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
        r1 = Rectangle(10, 10, 10, 10)
        r1.update()
        m = test_update.stdout_return(r1, "print")
        self.assertEqual(m.getvalue(), r1.__str__() + '\n')

    def test_one_arg(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        m = test_update.stdout_return(r1, "print")
        self.assertEqual(m.getvalue(), r1.__str__() + '\n')

    def test_two_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2)
        m = test_update.stdout_return(r1, "print")
        self.assertEqual(m.getvalue(), r1.__str__() + '\n')

    def test_3_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3)
        m = test_update.stdout_return(r1, "print")
        self.assertEqual(m.getvalue(), r1.__str__() + '\n')

    def test_4_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4)
        m = test_update.stdout_return(r1, "print")
        self.assertEqual(m.getvalue(), r1.__str__() + '\n')

    def test_5_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        m = test_update.stdout_return(r1, "print")
        self.assertEqual(m.getvalue(), r1.__str__() + '\n')

    def test_kwargs_height(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        m = test_update.stdout_return(r1, "print")
        self.assertEqual(m.getvalue(), r1.__str__() + '\n')

    def test_kwargs_id(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(id=98)
        m = test_update.stdout_return(r1, "print")
        self.assertEqual(m.getvalue(), r1.__str__() + '\n')

    def test_kwargs_2args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(width=1, x=2)
        m = test_update.stdout_return(r1, "print")
        self.assertEqual(m.getvalue(), r1.__str__() + '\n')

    def test_kwargs_3args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(y=1, width=2, x=3)
        m = test_update.stdout_return(r1, "print")
        self.assertEqual(m.getvalue(), r1.__str__() + '\n')

    def test_kwargs_4args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(y=1, width=2, x=3, id=89)
        m = test_update.stdout_return(r1, "print")
        self.assertEqual(m.getvalue(), r1.__str__() + '\n')

    def test_kwargs_5args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(y=2, width=6, x=4, id=90, height=5)
        m = test_update.stdout_return(r1, "print")
        self.assertEqual(m.getvalue(), r1.__str__() + '\n')

class test_create_method(unittest.TestCase):
    """unittest for the create method"""
    def test_creates_instance(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(type(r1), type(r2))

class test_save_load_file(unittest.TestCase):
    """unittest for the save_to_file method"""
    def test_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json") as f:
            self.assertEqual("[]", f.read())

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual("[]", f.read())

    def test_one_obj(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        m = '[{"id": 18, "width": 1, "height": 2, "x": 0, "y": 0}]'
        with open("Rectangle.json") as f:
            self.assertEqual(m, f.read())

    def test_file_no_exist(self):
        out = Rectangle.load_from_file()
        self.assertEqual([], out)

    def test_load_file_exists(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])
        out = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(out[0]))

    """
class test_load_from_file(unittest.TestCase):
    r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
            Rectangle.save_to_file([r1, r2])

                with open("Rectangle.json", "r") as file:
                            print(file.read())"""

if __name__ == "__main__":
    unittest.main()
