#!/usr/bin/python3
'''Create class rectangle'''


class Rectangle:
    '''Creates a rectangle object'''

    def __init__(self, width=0, height=0):
        '''Initialisation of object. Runs check to ensure value passed
        are good.'''
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        '''Return width of object.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set width of object.'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Return Height of object.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set value of height of object.'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Returns the area of the object.'''
        return self.height * self.width

    def perimeter(self):
        '''Returns to perimeter of object. If height or width = 0
        perimeter is 0'''
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height * 2) + (self.width * 2)
