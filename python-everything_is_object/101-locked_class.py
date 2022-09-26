#!/usr/bin/python3
class LockedClass:
    '''A locked class that only lets instance attribute of first_name'''
    __slots__ = ['first_name']
