#!/usr/bin/python3
'''
This module contains the rectangle class constructor.
'''

from models.base import Base


class Rectangle(Base):
    '''This module is the subclass from the Base class.'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Class initalisation method.'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Getter for width property.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Setter for width property. Checks to enusre the value passed through
        is an int and above 0.
        '''
        try:
            self.integer_validator('width', value)
            self.__width = value
        except Exception as e:
            raise e

    @property
    def height(self):
        '''Getter for height property.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Setter for height property. Checks to ensure value passed through is
        an int and above 0.
        '''
        try:
            self.integer_validator('height', value)
            self.__height = value
        except Exception as e:
            raise e

    @property
    def x(self):
        '''Getter for x property.'''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        Setter for x property. Checks to ensure value is an int and
        greater or equal to 0.
        '''
        try:
            self.integer_validator("x", value)
            self.__x = value
        except Exception as e:
            raise e

    @property
    def y(self):
        '''Getter for y property.'''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        Setter for y property. Checks to see if the value passed through
        is good.
        '''
        try:
            self.integer_validator("y", value)
            self.__y = value
        except Exception as e:
            raise e

    def display(self):
        '''
        This method prints out the rectangle.
        '''
        rect_string = ""
        for space in range(self.y):
            rect_string += '\n'
        for i in range(self.height):
            for space in range(self.x):
                rect_string += " "
            for character in range(self.width):
                rect_string += "#"
            if i != self.height - 1:
                rect_string += '\n'

        print(rect_string)

    def area(self):
        '''Returns the value of width * height of the instance.'''
        return (self.width * self.height)

    def __str__(self):
        '''This method returns a formatted string describing the instance.'''
        return (f'[{type(self).__name__}] ({self.id}) \
{self.x}/{self.y} - {self.width}/{self.height}')

    def update(self, *args, **kwargs):
        '''This method assigns values to the attribute depending on the
        positon it is entered. 1: id, 2: width, 3: height, 4: x, 5: y.
        '''
        if args is not None and len(args) > 0:
            attribute_tuple = ("id", "width", "height", "x", "y")
            for x in range(len(args)):
                setattr(self, attribute_tuple[x], args[x])
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, str(key), value)

    def integer_validator(self, name, value):
        '''
        This function checks the value passed through are int and greater
        than 0.
        '''
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if name in ['height', 'width']:
            if value <= 0:
                raise ValueError(f"{name} must be > 0")
        if name in ['x', 'y']:
            if value < 0:
                raise ValueError(f"{name} must be >= 0")
