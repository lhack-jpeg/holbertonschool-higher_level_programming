#!/usr/bin/python3
'''
Unit test for base class
'''

import re
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''Unittest for Base Class.'''
    def Test_obj_class(self):
        '''Test type of base.'''
        my_obj = Base()
        self.assertTrue(isinstance(my_obj, Base))

    def test_base_docs(self):
        '''Test base docs.'''
        module_docs = "models.base".__doc__
        self.assertTrue(len(module_docs) > 1)

        class_docs = Base.__doc__
        self.assertTrue(len(class_docs) > 1)

    @classmethod
    def setUpClass(cls):
        '''Set up test environment.'''
        Base._Base__nb_objects = 0
        cls.base_1 = Base()
        cls.base_2 = Base(id=36)
        cls.base_3 = Base()

    def test_obj_id(self):
        '''Test Base id assignment works.'''
        self.assertEqual(self.base_1.id, 1)
        self.assertEqual(self.base_2.id, 36)
        self.assertEqual(self.base_3.id, 2)

    def test_base_to_json_string(self):
        '''Test class methods for Json string.'''
        test_dict = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        result = Base.to_json_string(test_dict)
        self.assertTrue(isinstance(result, str))
        result = Base.to_json_string(None)
        self.assertEqual(result, '[]')
        result = Base.to_json_string([])
        self.assertEqual(result, '[]')

    def test_base_from_json_string(self):
        '''Test method from json string.'''
        result = Base.from_json_string(None)
        self.assertEqual(result, [])
        self.assertTrue(isinstance(result, list))
        result = Base.from_json_string('[]')
        self.assertEqual(result, [])
        self.assertTrue(isinstance(result, list))
        result = Base.from_json_string('[{"id": 2, "width": 20}]')
        self.assertTrue(isinstance(result, list))
        self.assertEqual(result, [{"id": 2, "width": 20}])


if __name__ == "__main__":
    unittest.main()
