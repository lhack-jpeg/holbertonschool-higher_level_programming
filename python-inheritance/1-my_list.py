#!/usr/bin/python3
'''
This module contains the class constructor that
inherits from Pythons Builtin object lists.
'''


class MyList(list):
    '''
    This class inherits from lists super class has new method
    to sort and print out list.
    '''

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        '''
        This method sorts the list and prints it out.
        '''
        print(sorted(self))
