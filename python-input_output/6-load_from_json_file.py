#!/usr/bin/python3
'''
This module contains the function to return an object from
a file
'''


import json


def load_from_json_file(filename):
    '''
    wrapper function
    '''
    with open(filename, 'r', encoding='utf-8') as f:
        json.load(filename)
