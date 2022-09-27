#!/usr/bin/python3
'''This module contains the constructor for class
BaseGeometry
'''


class BaseGeometry:
    '''
    Creates an object from base geometry class
    '''
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
