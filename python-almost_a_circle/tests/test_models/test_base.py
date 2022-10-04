#!/usr/bin/python3
'''
Unit test for base class
'''

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def Test_obj_class(self):
        my_obj = Base()
        self.assertTrue(isinstance(my_obj, Base))

    def test_base_docs(self):
        module_docs = "models.base".__doc__
        self.assertTrue(len(module_docs) > 1)

        class_docs = Base.__doc__
        self.assertTrue(len(class_docs) > 1)

    def test_obj_id(self):
        my_obj = Base()
        my_obj_2 = Base(24)
        my_obj_3 = Base()
        self.assertEqual(my_obj.id, 1)
        self.assertEqual(my_obj_2.id, 24)
        self.assertEqual(my_obj_3.id, 2)

if __name__ == "__main__":
    unittest.main()
