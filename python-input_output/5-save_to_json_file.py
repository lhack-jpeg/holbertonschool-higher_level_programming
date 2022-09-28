#!/usr/bin/python3
'''
This module contains the function to save objects to
txt file
'''


import json


def save_to_json_file(my_obj, filename):
    '''
    wrapper function
    '''
    with open(filename, 'a', encoding="utf-8") as f:
        json.dump(my_obj, f)
