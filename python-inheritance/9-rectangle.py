#!/usr/bin/python3
'''
This module contains the constructor that inherits from
the BaseGeometry Class.
'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle class constructor'''
    def __init__(self, width, height):
        try:
            self.integer_validator('width', width)
            self.__width = width
        except Exception as e:
            raise e

        try:
            self.integer_validator('height', height)
            self.__height = height
        except Exception as e:
            raise e

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return (f'[{type(self).__name__}] {self.__width}/{self.__height}')
