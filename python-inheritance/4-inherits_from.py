#!/usr/bin/python3
'''
Module contains one function to checkif object is
subclass
'''


def inherits_from(obj, a_class):
    '''
    function return is subclass func
    '''
    sub_c = issubclass(type(obj), a_class)
    is_c = type(obj) == a_class
    if sub_c & ~is_c:
        return True
    else:
        return False
