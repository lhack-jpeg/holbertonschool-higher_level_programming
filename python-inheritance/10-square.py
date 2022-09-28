#!/usr/bin/python3
'''
This module contains the constructor that inherits from
the BaseGeometry Class and the Rectangle class.
'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Square class constructor'''
    def __init__(self, size):
        try:
            self.integer_validator('size', size)
            self.__size = size
        except Exception as e:
            raise e

    def area(self):
        return (self.__size ** 2)

    def __str__(self):
        return (f'[Square] {self.__size}/{self.__size}')
