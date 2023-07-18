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

    """
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
