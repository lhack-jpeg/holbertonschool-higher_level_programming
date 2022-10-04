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

        class_docs = Rectangle.__doc__
        self.assertTrue(len(class_docs) > 1)

    def test_obj_class(self):
        my_obj = Rectangle(10, 2)
        self.assertTrue(isinstance(my_obj, Rectangle))

        self.assertTrue(issubclass(type(my_obj), Base))

    def test_obj_id(self):
        my_obj = Rectangle(10, 2)
        my_obj_2 = Rectangle(4, 12, 0, 0, 24)
        self.assertEqual(my_obj.id, 4)
        self.assertEqual(my_obj_2.id, 24)

    def test_right_type(self):
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
        test_obj = Rectangle(4, 5)
        self.assertEqual(test_obj.area(), 20)

        test_obj.width = 6
        self.assertEqual(test_obj.area(), 30)


if __name__ == "__main__":
    unittest.main()
