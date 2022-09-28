#!/usr/bin/python3
'''
This module contains one function to return JSON object.
'''


import json


def to_json_string(my_obj):
    '''
    wrapper function.
    '''
    return json.dumps(my_obj)
