#!/usr/bin/python3
"""
the unittest model
Unittest for max_integer()
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """
    unittest class that contains methods to test max_integer()
    """
    def test_mod(self):
        """tests the module's docstring"""
        mod = __import__("6-max_integer").__doc__
        self.assertTrue(len(mod) > 1)

    def test_func(self):
        """tests the function's docstring"""
        func = __import__("6-max_integer").max_integer.__doc__
        self.assertTrue(len(func) > 1)

    def test_max_beginning(self):
        """tests while the max int is at the beginning"""
        a = [22, 2, 3, 10, 15]
        self.assertEqual(max_integer(a), 22)

    def test_max_end(self):
        """tests while the max int is at the end"""
        a = [1, 2, 3, 10, 15]
        self.assertEqual(max_integer(a), 15)

    def test_max_mid(self):
        """tests while max is in the middle"""
        a = [1, 2, 20, 10, 15]
        self.assertEqual(max_integer(a), 20)

    def test_negAndpos(self):
        """tests with negative and positive values"""
        a = [-1, 2, -20, 10, -15]
        self.assertEqual(max_integer(a), 10)

    def test_allNegative(self):
        """ tests with all negative values"""
        a = [-1, -2, -20, -10, -15]
        self.assertEqual(max_integer(a), -1)

    def test_not_int(self):
        """tests for non int argument"""
        a = [1, 2, 3, "4", 5]
        with self.assertRaises(TypeError):
            max_integer(a)

    def test_not_list(self):
        """tests if arg is not a list"""
        with self.assertRaises(TypeError):
            max_integer(4)

    def test_empty(self):
        """tests if list is empty"""
        a = []
        self.assertIsNone(max_integer(a))

    def test_None(self):
        """tests if None is passed as arg"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_no_args(self):
        """tests if no args are passed"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """tests if only 1 element is in list"""
        a = [10]
        self.assertEqual(max_integer(a), 10)

if __name__ == '__main__':
    unittest.main()
