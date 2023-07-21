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

class test_save_load_csv(unittest.TestCase):
    """ unittest class to test save_to_csv_file and
    load_from_csv_file"""
    def test_save_1_obj(self):
        r1 = Rectangle(10, 3, 2, 6, 5)
        Rectangle.save_to_file_csv([r1])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,3,2,6", f.read())

    def test_save_2_objs(self):
        r1 = Square(10, 7, 2, 8)
        r2 = Square(10, 4, 1, 2)
        Square.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("8,10,7,2\n2,4,10,4,1", f.read())

    def test_load_1_obj(self):
        s1 = Square(2, 1, 4, 3)
        s2 = Square(10, 5, 6, 3)
        Square.save_to_file_csv([s1, s2])
        out = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(out[0]))

    def test_check_all_types(self):
        r1 = Rectangle(1, 8, 2, 9, 1)
        r2 = Rectangle(5, 3, 7, 4, 6)
        r3 = Rectangle(2, 3, 5, 6, 3)
        Rectangle.save_to_file_csv([r1, r2, r3])
        out = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in out))

if __name__ == "__main__":
    unittest.main()
