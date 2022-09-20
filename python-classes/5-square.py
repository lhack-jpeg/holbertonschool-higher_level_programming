#!/usr/bin/python3
'''Write a class that defines a square by the size attribute.'''


class Square:
    '''Creates an initalised object'''
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Returns the value of __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter property to update the private field."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the value of the size squared."""
        return self.__size ** 2

    def my_print(self):
        """Prints to the STDOUT the square, newline if size = 0."""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
