#!/usr/bin/python3
'''
This module contains one function to turn JSON
to python Object.
'''

import json


def from_json_string(my_str):
    '''
    wrapper function
    '''
    return json.loads(my_str)
