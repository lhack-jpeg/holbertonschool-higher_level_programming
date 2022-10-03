#!/usr/bin/python3
'''
This module contains the constructor for the base class
'''


class Base():
    '''
    Constructor for base class
    '''
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
