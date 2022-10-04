#!/usr/bin/python3

'''
Unit testing for the square class
'''

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class testSquare(unittest.TestCase):
     def test_rectangle_docs(self):
          module_docs = "models.square".__doc__
          self.assertTrue(len(module_docs) > 1)

          class_docs = Square.__doc__
          self.assertTrue(len(class_docs) > 1)

     def test_obj_class(self):
         my_obj = Square(5)
         self.assertTrue(isinstance(my_obj, Square))
         self.assertTrue(issubclass(type(my_obj), Rectangle))

     def test_obj_id(self):
          my_obj = Square(10)
          my_obj_2 = Square(4, 0, 0, 24)
          self.assertEqual(my_obj.id, 2)
          self.assertEqual(my_obj_2.id, 24)
