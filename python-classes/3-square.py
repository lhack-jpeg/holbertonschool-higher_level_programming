#!/usr/bin/python3
'''Write a class that defines a square by the size attribute.'''


class Square:
    '''Creates an initalised object'''
    def __init__(self, size=0):
        """size must be an integer, otherwise raise a TypeError exception with
        the message size must be an integer
        if size is less than 0, raise a ValueError exception with the message
        size must be >= 0."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the value of the size squared."""
        return self.__size ** 2
