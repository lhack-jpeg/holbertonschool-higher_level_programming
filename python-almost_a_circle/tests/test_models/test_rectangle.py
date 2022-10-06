#!/usr/bin/python3

'''
Unit test for the rectangle class
'''

import unittest
import inspect
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleDocs(unittest.TestCase):
    """ Testing class Rectangle for documentation """

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.rect_funcs = inspect.getmembers(Rectangle, inspect.isfunction)

    def test_base_docs(self):
        """ checking for docs """
        module_docs = "models.rectangle".__doc__
        self.assertTrue(len(module_docs) > 1)

        class_docs = Rectangle.__doc__
        self.assertTrue(len(class_docs) > 1)

    def test_module_docstr(self):
        """Tests for docstring"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_class_docstr(self):
        """Tests for docstring"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for docstrings in all functions"""
        for func in self.rect_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestRectangle(unittest.TestCase):
    '''Testing Rectangle methods.'''

    @classmethod
    def setUpClass(cls):
        '''Set up test environment.'''
        Base._Base__nb_objects = 0
        cls.r1 = Rectangle(10, 4, id=4)
        cls.r2 = Rectangle(5, 4)
        cls.r3 = Rectangle(4, 12, 0, 0, 24)
        cls.r4 = Rectangle(6, 8)

    def test_obj_class(self):
        '''Test to see class and inheritance.'''
        self.assertTrue(isinstance(self.r1, Rectangle))
        self.assertTrue(issubclass(type(self.r1), Base))

    def test_obj_id(self):
        '''Test init method.'''
        self.assertEqual(self.r1.id, 4)
        self.assertEqual(self.r2.id, 2)

    def test_right_type(self):
        '''Test integer validator method.'''
        with self.assertRaises(TypeError):
            my_obj = Rectangle("Hello World", 2)

        with self.assertRaises(TypeError):
            my_obj = Rectangle(2, [2])

        with self.assertRaises(TypeError):
            my_obj = Rectangle(2, 12, 0, "1")

        with self.assertRaises(TypeError):
            my_obj = Rectangle(2, 12, 1, None)

        with self.assertRaises(TypeError):
            my_obj = Rectangle(2, 4)
            my_obj.height = "1"

        with self.assertRaises(TypeError):
            my_obj = Rectangle(2, 4)
            my_obj.width = "School"

        with self.assertRaises(TypeError):
            my_obj = Rectangle(2, 4)
            my_obj.y = [1]

        with self.assertRaises(TypeError):
            my_obj = Rectangle(2, 4)
            my_obj.x = (1, 2)

    def test_good_value(self):
        '''test integer validator.'''
        with self.assertRaises(ValueError):
            my_obj = Rectangle(2, -2)

        with self.assertRaises(ValueError):
            my_obj = Rectangle(2, 2, 0, -1, 24)

        with self.assertRaises(ValueError):
            my_obj = Rectangle(2, 12, -1, 1, 36)

        with self.assertRaises(ValueError):
            my_obj = Rectangle(2, 0, 0, -1, 24)

        with self.assertRaises(ValueError):
            my_obj = Rectangle(1, 2)
            my_obj.width = -1

        with self.assertRaises(ValueError):
            my_obj.height = 0

        with self.assertRaises(ValueError):
            my_obj.x = -1

        with self.assertRaises(ValueError):
            my_obj.y = -1

    def test_rectangle_area(self):
        '''Test the return from area method.'''
        self.assertEqual(self.r2.area(), 20)

        self.r2.width = 6
        self.assertEqual(self.r2.area(), 30)

    def test_rectangle_update(self):
        '''Check update method with *args.'''
        self.r3.update(42)
        self.assertEqual(self.r3.id, 42)
        self.r3.update(42, 2)
        self.assertEqual(self.r3.width, 2)
        self.r3.update(42, 2, 8)
        self.assertEqual(self.r3.height, 8)
        self.r3.update(42, 2, 8, 9)
        self.assertEqual(self.r3.x, 9)

        with self.assertRaises(ValueError):
            self.r3.update(42, 2, 8, 9, -10)

    def test_rectangle_kwargs(self):
        '''Function to test kwargs method.'''
        self.r1.update(id=42)
        self.assertEqual(self.r1.id, 42)
        self.r1.update(y=1, x=2)
        self.assertEqual(self.r1.x, 2)
        self.assertEqual(self.r1.y, 1)
        self.r1.update(height=20, width=12)
        self.assertEqual(self.r1.height, 20)
        self.assertEqual(self.r1.width, 12)

        with self.assertRaises(ValueError):
            self.r2.update(height=0)

    def test_rect_str(self):
        '''test __str__ method'''
        self.assertTrue(isinstance(str(self.r3), str))
        self.assertEqual(str(self.r3), '[Rectangle] (24) 0/0 - 4/12')

    def test_rect_to_dictionary(self):
        '''Test to_dictionary method.'''
        test_dict = {'id': 4, 'width': 10, 'height': 4, 'x': 0, 'y': 0}
        r1_dict = self.r1.to_dictionary()
        self.assertTrue(isinstance(r1_dict, dict))
        self.assertEqual(r1_dict, test_dict)


if __name__ == "__main__":
    unittest.main()
