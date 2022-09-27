#!/usr/bin/python3
'''
Module contains one function to checkif object is
subclass
'''


def inherits_from(obj, a_class):
    '''
    function return is subclass func
    '''
    return issubclass(type(obj), a_class)
