#!/usr/bin/python3

'''
Unit test for the rectangle class
'''

import io
import unittest
import unittest.mock
import inspect
import os
import json
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
            if len(func[1].__doc__) < 1:
                print(func)
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
        cls.r4 = Rectangle(6, 8, 2)

    def test_obj_class(self):
        '''Test to see class and inheritance.'''
        self.assertTrue(isinstance(self.r1, Rectangle))
        self.assertTrue(issubclass(type(self.r1), Base))

    def test_obj_id(self):
        '''Test init method.'''
        self.assertEqual(self.r1.id, 4)
        self.assertEqual(self.r2.id, 1)
        self.assertEqual(self.r4.id, 2)

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
            my_obj = Rectangle(0, 2)

        with self.assertRaises(ValueError):
            my_obj = Rectangle(2, 0)

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
        self.assertEqual(self.r2.area(), 24)
        
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, expected_output, mock_stdout):
        '''Test display method of class.'''
        self.r2.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        self.r4.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

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
            self.r3.update(42, 2, -8, 9, 10)

    def test_rectangle_kwargs(self):
        '''Function to test kwargs method.'''
        self.r1.update(**{'id': 42})
        self.assertEqual(self.r1.id, 42)
        self.r1.update(**{'id': 42, 'height': 20})
        self.assertEqual(self.r1.height, 20)
        self.r1.update(**{'id': 42, 'height': 20, 'width': 20})
        self.assertEqual(self.r1.width, 20)
        self.r1.update(**{'id': 42, 'height': 20, 'width': 20, 'x': 2})
        self.assertEqual(self.r1.x, 2)
        self.r1.update(**{'id': 42, 'height': 20, 'width': 20, 'x': 2, 'y': 1})
        self.assertEqual(self.r1.y, 1)

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

    def test_rect_create(self):
        '''Test class method from Base using using rectangle class.'''
        r2_dict = self.r2.to_dictionary()
        clone_r2 = Rectangle.create(**r2_dict)
        self.assertEqual(r2_dict, clone_r2.to_dictionary())
        new_r = Rectangle.create(**{'id': 1024})
        self.assertTrue(isinstance(new_r, Rectangle))
        self.assertEqual(
            new_r.to_dictionary(),
            {'id': 1024, 'width': 1, 'height': 1, 'x': 0, 'y': 0})
        new_r = Rectangle.create(**{'id': 1024, 'height': 2})
        self.assertTrue(isinstance(new_r, Rectangle))
        self.assertEqual(
            new_r.to_dictionary(),
            {'id': 1024, 'height': 2, 'width': 1, 'x': 0, 'y': 0})
        new_r = Rectangle.create(
            **{'id': 1024, 'height': 2, 'width': 12})
        self.assertTrue(isinstance(new_r, Rectangle))
        self.assertEqual(
            new_r.to_dictionary(),
            {'id': 1024, 'height': 2, 'width': 12, 'x': 0, 'y': 0})
        new_r = Rectangle.create(
            **{'id': 1024, 'height': 2, 'width': 12, 'x': 2})
        self.assertTrue(isinstance(new_r, Rectangle))
        self.assertEqual(
            new_r.to_dictionary(),
            {'id': 1024, 'height': 2, 'width': 12, 'x': 2, 'y': 0})
        new_r = Rectangle.create(
            **{'id': 1024, 'height': 2, 'width': 12, 'x': 2, 'y': 1})
        self.assertTrue(isinstance(new_r, Rectangle))
        self.assertEqual(
            new_r.to_dictionary(),
            {'id': 1024, 'height': 2, 'width': 12, 'x': 2, 'y': 1})

    def test_rect_save_to_file(self):
        '''Test save to file method for Rectangle class.'''
        '''Check it saves and empty string'''
        filename = 'Rectangle.json'
        Rectangle.save_to_file(None)
        with open(filename, 'r', encoding='utf-8') as f:
            result = f.read()
            self.assertEqual(result, '[]')
        '''clean up file.'''
        if os.path.exists(filename):
            os.remove(filename)
            Rectangle.save_to_file([])
        with open('Rectangle.json', 'r', encoding='utf-8') as f:
            result = f.read()
            self.assertEqual(result, '[]')
        '''clean up file.'''
        if os.path.exists(filename):
            os.remove(filename)
        Rectangle.save_to_file([self.r1])
        self.assertTrue(os.path.exists(filename))
        with open(filename, 'r', encoding='utf-8') as f:
            result = f.read()
            result = json.loads(result)
            self.assertEqual(result, [self.r1.to_dictionary()])
        if os.path.exists(filename):
            os.remove(filename)

    def test_rect_load_from_file(self):
        '''Test load from file method.'''
        filename = 'Rectangle.json'
        if os.path.exists(filename):
            os.remove(filename)
        result = Rectangle.load_from_file()
        self.assertEqual(result, [])
        Rectangle.save_to_file([self.r3])
        result = Rectangle.load_from_file()
        self.assertEqual(str(result[0]), str(self.r3))


if __name__ == "__main__":
    unittest.main()
