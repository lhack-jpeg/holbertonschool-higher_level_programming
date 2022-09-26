#!/usr/bin/python3
'''
This module contains one function that returns a list
of every attribute and method of an object.
'''


def lookup(obj):
    '''
    Function takes the object and returns a list of attributes
    and methods.
    '''
    return (dir(obj))
