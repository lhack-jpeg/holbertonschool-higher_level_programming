#!/usr/bin/python3
'''Write a class that defines a square by the size attribute.'''


class Square:
    '''Creates an initalised object'''
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        """Returns value of position tuple"""
        return self.__position

    @position.setter
    def positon(self, value):
        """Sets value of position attribute"""
        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """Returns the value of the size squared."""
        return self.__size ** 2

    def my_print(self):
        """Prints to the STDOUT the square, newline if size = 0."""
        if self.__size == 0:
            print()
        else:
            if self.position[1] > 0:
                for i in range(0, self.position[1]):
                    print()
            for j in range(0, self.__size):
                for space in range(self.position[0]):
                    print(" ", end="")
                for sign in range(self.__size):
                    print("#", end="")
                print()
