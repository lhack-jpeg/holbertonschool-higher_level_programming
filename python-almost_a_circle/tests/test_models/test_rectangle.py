#!/usr/bin/python3

'''
Unit test for the rectangle class
'''

import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_rectangle_docs(self):
        module_docs = "models.rectangle".__doc__
        self.assertTrue(len(module_docs) > 1)

        class_docs = Recctangle.__doc__
        self.assertTrue(len(class_docs) > 1)

    def test_obj_class(self):
        my_obj = Rectangle(10, 2)
        self.assertTrue(isinstance(my_obj, Rectangle))

        self.assertTrue(issubclass(my_obj, Base))

    def test_obj_id(self):
        my_obj = Rectangle(10, 2)
        my_obj = Rectangle(4, 12, 0, 0, 24)
        self.assertEqual(my_obj.id, 1)
        self.assertEqual(my_obj_2.id, 24)


if __name__ == "__main__":
    unittest.main()
