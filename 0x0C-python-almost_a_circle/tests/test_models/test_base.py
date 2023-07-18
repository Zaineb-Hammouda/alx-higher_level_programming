#!/usr/bin/python3
"""
unittest model
Unittest for Base()
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    unittest class to test the Base class
    """
    def test_0_args(self):
        """test for no arguments to Base"""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_arg_None(self):
        """test for passing none"""
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def test_id(self):
        b = Base(89)
        self.assertEqual(89, b.id)

    def test_idPublic(self):
        b = Base(89)
        b.id = 5
        self.assertEqual(5, b.id)

    def test_nb_instances(self):
        with self.assertRaises(AttributeError):
            print(Base(3).__nb_instances)

    def test_id_no_arg(self):
        a = Base()
        b = Base(98)
        c = Base()
        self.assertEqual(a.id, c.id - 1)

class test_to_json_string(unittest.TestCase):
    """unittest class to test to_json_string method"""
    def test_type(self):
        r1 = Rectangle(10, 7, 2, 8)
        j_dict = Base.to_json_string([r1.to_dictionary()])
        self.assertEqual(str, type(j_dict))

    def test_None(self):
        j_dict = Base.to_json_string(None)
        self.assertEqual("[]", j_dict)

    def test_empty(self):
        j_dict = Base.to_json_string([])
        self.assertEqual("[]", j_dict)

    def test_return(self):
        j_dict = Base.to_json_string([{'id': 12}])
        self.assertEqual('[{"id": 12}]', j_dict)

class test_from_json_srting(unittest.TestCase):
    """unittest class to test from_json_string method"""
    def test_empty_string(self):
        output = Rectangle.from_json_string("[]")
        self.assertEqual([], output)

    def test_None_input(self):
        output = Rectangle.from_json_string(None)
        self.assertEqual([], output)

    def test_return_list(self):
        j_list = Base.from_json_string('[{"id": 12}]')
        self.assertEqual([{'id': 12}], j_list)
