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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''Getter for width property.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter for width property.'''
        self.__width = value

    @property
    def height(self):
        '''Getter for height property.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter for height property.'''
        self.__height = value

    @property
    def x(self):
        '''Getter for x property.'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Setter for x property.'''
        self.__x = value

    @property
    def y(self):
        '''Getter for y property.'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Setter for y property.'''
        self.__y = value
