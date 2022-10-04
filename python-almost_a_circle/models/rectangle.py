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
            self.height_width_validator('width', value)
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
            self.height_width_validator('height', value)
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
            self.x_y_validator("x", value)
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
            self.x_y_validator("y", value)
            self.__y = value
        except Exception as e:
            raise e

    def display(self):
        '''
        This method prints out the rectangle.
        '''
        rect_string = ""
        for i in range(self.height):
            for j in range(self.width):
                rect_string += "#"
            if i != self.height - 1:
                rect_string += '\n'

        print (rect_string)


    def height_width_validator(self, name, value):
        '''
        This function checks the value passed through are int and greater
        than 0.
        '''
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def x_y_validator(self, name, value):
        '''
        This function checks the value passed through are int and greater
        than  or equal to 0.
        '''
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")

        if value < 0:
            raise ValueError(f"{name} must be >= 0")
