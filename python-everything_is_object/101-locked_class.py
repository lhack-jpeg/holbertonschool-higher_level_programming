#!/usr/bin/python3
'''This module contains the constructor used to create a lockedclass
object'''


class LockedClass:
    '''A locked class that only lets instance attribute of first_name'''
    __slots__ = ['first_name']
