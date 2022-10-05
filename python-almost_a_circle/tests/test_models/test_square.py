#!/usr/bin/python3

'''
Unit testing for the square class
'''

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class testSquare(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0
        cls.sq_1 = Square(5)
        cls.sq_2 = Square(2, id=24)
        cls.sq_3 = Square(4, 1, 6)

    def test_rectangle_docs(self):
        module_docs = "models.square".__doc__
        self.assertTrue(len(module_docs) > 1)

        class_docs = Square.__doc__
        self.assertTrue(len(class_docs) > 1)

    def test_obj_class(self):
        self.assertTrue(isinstance(self.sq1, Square))
        self.assertTrue(issubclass(type(self.sq_1), Rectangle))

    def test_obj_id(self):
        '''Check to assignment of id with None passed.'''
        self.assertEqual(self.sq_1.id, 1)
        '''Check to assignment of id with id passed.'''
        self.assertEqual(self.sq_2.id, 24)
        '''Check to assignment of id with None passed + 1.'''
        self.assertEqual(self.sq_3.id, 2)

    def test_obj_setter_getter(self):
        '''Check the setter and getter for size property.'''
        self.assertEqual(self.sq_1.size, 5)
        self.sq_1.size = 3
        self.assertEqual(self.sq_1.size, 3)
        self.assertEqual(self.sq_2.x, 1)
        self.sq_1.x = 4
        self.assertEqual(self.sq_2.x, 4)
        self.sq_1.y = 10
        self.assertEqual(self.sq_2.y, 4)

        with self.assertRaises(TypeError):
            '''Check integer validator method works within setter.'''
            self.sq_1.size = '4'

        with self.assertRaises(ValueError):
            '''Check integer validator method works within setter.'''
            self.sq_1.size = 0


if __name__ == "__main__":
    unittest.main()
