#!/usr/bin/python3
"""
unittest model
Unittest for Base()
"""
import unittest
from models.base import Base


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

    """def test_ 
    def test_max_beginning(self):
        a = [22, 2, 3, 10, 15]
        self.assertEqual(max_integer(a), 22)

    def test_max_end(self):
        a = [1, 2, 3, 10, 15]
        self.assertEqual(max_integer(a), 15)

    def test_max_mid(self):
        a = [1, 2, 20, 10, 15]
        self.assertEqual(max_integer(a), 20)

    def test_negAndpos(self):
        a = [-1, 2, -20, 10, -15]
        self.assertEqual(max_integer(a), 10)

    def test_allNegative(self):
        a = [-1, -2, -20, -10, -15]
        self.assertEqual(max_integer(a), -1)

    def test_not_int(self):
        a = [1, 2, 3, "4", 5]
        with self.assertRaises(TypeError):
            max_integer(a)

    def test_not_list(self):
        with self.assertRaises(TypeError):
            max_integer(4)

    def test_empty(self):
        a = []
        self.assertIsNone(max_integer(a))

    def test_None(self):
        with self.assertRaises(TypeError):
            max_integer(None)
	"""
