#!/usr/bin/python3

'''
Unit testing for the square class
'''

from turtle import clone
import unittest
import inspect
import os
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangleDocs(unittest.TestCase):
    """ Testing class Rectangle for documentation """

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.rect_funcs = inspect.getmembers(Square, inspect.isfunction)

    def test_base_docs(self):
        """ checking for docs """
        module_docs = "models.square".__doc__
        self.assertTrue(len(module_docs) > 1)

        class_docs = Square.__doc__
        self.assertTrue(len(class_docs) > 1)

    def test_module_docstr(self):
        """Tests for docstring"""
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_class_docstr(self):
        """Tests for docstring"""
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for docstrings in all functions"""
        for func in self.rect_funcs:
            if len(func[1].__doc__) < 1:
                print(func)
            self.assertTrue(len(func[1].__doc__) >= 1)


class testSquare(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        '''Set up test environment.'''
        Base._Base__nb_objects = 0
        cls.sq_1 = Square(5)
        cls.sq_2 = Square(2, id=24)
        cls.sq_3 = Square(4, 2)
        cls.sq_4 = Square(3, 2, 4)

    def test_obj_class(self):
        '''Check to see instances of classes and inheritance.'''
        self.assertTrue(isinstance(self.sq_1, Square))
        self.assertTrue(issubclass(type(self.sq_1), Rectangle))

    def test_square_obj_id(self):
        Base._Base__nb_objects = 0
        '''Check to assignment of id with None passed.'''
        self.assertEqual(self.sq_1.id, 22)
        '''Check to assignment of id with id passed.'''
        self.assertEqual(self.sq_2.id, 24)
        '''Check to assignment of id with None passed + 1.'''
        self.assertEqual(self.sq_3.id, 42)

    def test_square_obj_setter_getter(self):
        '''Check the setter and getter for size property.'''
        self.assertEqual(self.sq_1.size, 6)
        self.sq_1.size = 3
        self.assertEqual(self.sq_1.size, 3)
        self.assertEqual(self.sq_2.x, 0)
        self.sq_1.x = 7
        self.assertEqual(self.sq_1.x, 7)
        self.sq_1.y = 9
        self.assertEqual(self.sq_1.y, 9)

        with self.assertRaises(TypeError):
            '''Check integer validator method works within setter.'''
            self.sq_1.size = '4'

        with self.assertRaises(ValueError):
            '''Check integer validator method works within setter.'''
            self.sq_1.size = 0

    def test_square_right_type(self):
        '''Test integer validator method.'''
        with self.assertRaises(TypeError):
            my_obj = Square("Hello World", 2)

        with self.assertRaises(TypeError):
            my_obj = Square(2, [2])

        with self.assertRaises(TypeError):
            my_obj = Square(2, 12, "1")

        with self.assertRaises(TypeError):
            my_obj = Square(2, None)

        with self.assertRaises(TypeError):
            my_obj = Square(2, 4)
            my_obj.size = "1"

        with self.assertRaises(TypeError):
            my_obj = Square(2, 4)
            my_obj.size = "School"

        with self.assertRaises(TypeError):
            my_obj = Square(2, 4)
            my_obj.y = [1]

        with self.assertRaises(TypeError):
            my_obj = Square(2, 4)
            my_obj.x = (1, 2)

        with self.assertRaises(TypeError):
            my_obj = Square(1)
            my_obj.x = (1, 2)

    def test_square_good_value(self):
        '''test integer validator.'''
        with self.assertRaises(ValueError):
            my_obj = Square(-2)

        with self.assertRaises(ValueError):
            my_obj = Square(2, -1, id=24)

        with self.assertRaises(ValueError):
            my_obj = Square(-1)

        with self.assertRaises(ValueError):
            my_obj = Square(1, -1)

        with self.assertRaises(ValueError):
            my_obj = Square(1, 2, -1)

        with self.assertRaises(ValueError):
            my_obj = Square(0)

        with self.assertRaises(ValueError):
            my_obj = Square(2, -1, 0, 24)

        with self.assertRaises(ValueError):
            my_obj = Square(1, 2)
            my_obj.size = -1

        with self.assertRaises(ValueError):
            my_obj.size = 0

        with self.assertRaises(ValueError):
            my_obj.x = -1

        with self.assertRaises(ValueError):
            my_obj.y = -1

    def test_square_area(self):
        '''Test the return from area method.'''
        self.assertEqual(self.sq_1.area(), 25)

        self.sq_1.size = 6
        self.assertEqual(self.sq_1.area(), 36)

    def test_square_update(self):
        '''Check update method with *args.'''
        self.sq_2.update(42)
        self.assertEqual(self.sq_2.id, 42)
        self.sq_2.update(42, 2)
        self.assertEqual(self.sq_2.size, 2)
        self.sq_2.update(42, 2, 8)
        self.assertEqual(self.sq_2.x, 8)
        self.sq_2.update(42, 2, 8, 9)
        self.assertEqual(self.sq_2.y, 9)

        with self.assertRaises(ValueError):
            self.sq_2.update(42, 2, -8, 9)

    def test_square_kwargs(self):
        '''Function to test kwargs method.'''
        self.sq_3.update(**{'id': 42})
        self.assertEqual(self.sq_3.id, 42)
        self.sq_3.update(**{'id': 42, 'size': 20})
        self.assertEqual(self.sq_3.size, 20)
        self.sq_3.update(**{'id': 42, 'height': 20, 'x': 2})
        self.assertEqual(self.sq_3.x, 2)
        self.sq_3.update(**{'id': 42, 'height': 20, 'x': 2, 'y': 1})
        self.assertEqual(self.sq_3.y, 1)

        with self.assertRaises(ValueError):
            self.sq_3.update(height=0)

    def test_square_str(self):
        '''test __str__ method'''
        self.assertTrue(isinstance(str(self.sq_1), str))
        self.assertEqual(str(self.sq_1), '[Square] (22) 7/9 - 3')

    def test_square_to_dictionary(self):
        '''Test to_dictionary method.'''
        test_dict = {'id': 22, 'size': 3, 'x': 7, 'y': 9}
        sq_1_dict = self.sq_1.to_dictionary()
        self.assertTrue(isinstance(sq_1_dict, dict))
        self.assertEqual(sq_1_dict, test_dict)

    def test_square_create(self):
        '''Test class method from Base using using square class.'''
        sq_dict = self.sq_1.to_dictionary()
        clone_sq = Square.create(**sq_dict)
        self.assertEqual(sq_dict, clone_sq.to_dictionary())
        clone_sq = Square.create(**{'id': 1024})
        self.assertTrue(isinstance(clone_sq, Square))
        self.assertEqual(
            clone_sq.to_dictionary(),
            {'id': 1024, 'size': 1, 'x': 0, 'y': 0})
        clone_sq = Square.create(**{'id': 1024, 'size': 2})
        self.assertEqual(
            clone_sq.to_dictionary(),
            {'id': 1024, 'size': 2, 'x': 0, 'y': 0})
        clone_sq = Square.create(
            **{'id': 1024, 'size': 2, 'x': 2})
        self.assertEqual(
            clone_sq.to_dictionary(),
            {'id': 1024, 'size': 2, 'x': 2, 'y': 0})
        clone_sq = Square.create(
            **{'id': 1024, 'size': 2, 'x': 2, 'y': 5})
        self.assertEqual(
            clone_sq.to_dictionary(),
            {'id': 1024, 'size': 2, 'x': 2, 'y': 5})

    def test_square_save_to_file(self):
        '''Test save to file method for Rectangle class.'''
        '''Check it saves and empty string'''
        filename = 'Square.json'
        Square.save_to_file(None)
        with open(filename, 'r', encoding='utf-8') as f:
            result = f.read()
            self.assertEqual(result, '[]')
        '''clean up file.'''
        if os.path.exists(filename):
            os.remove(filename)
            Square.save_to_file([])
        with open(filename, 'r', encoding='utf-8') as f:
            result = f.read()
            self.assertEqual(result, '[]')
        '''clean up file.'''
        if os.path.exists(filename):
            os.remove(filename)
        Square.save_to_file([self.sq_1])
        self.assertTrue(os.path.exists(filename))
        with open(filename, 'r', encoding='utf-8') as f:
            result = f.read()
            result = json.loads(result)
            self.assertEqual(result, [self.sq_1.to_dictionary()])
        if os.path.exists(filename):
            os.remove(filename)

    def test_square_load_from_file(self):
        '''Test load from file method.'''
        filename = 'Square.json'
        if os.path.exists(filename):
            os.remove(filename)
        result = Square.load_from_file()
        self.assertEqual(result, [])
        Square.save_to_file([self.sq_3])
        result = Square.load_from_file()
        self.assertEqual(str(result[0]), str(self.sq_3))


if __name__ == "__main__":
    unittest.main()
