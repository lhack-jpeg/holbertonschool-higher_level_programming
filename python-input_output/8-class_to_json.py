#!/usr/bin/python3
'''
This function returns a dictionary description for JSON
serialisation of an object.
'''


import json


def class_to_json(obj):
    '''Take an object and returns a dict description of the obj.'''
    return json.dumps(obj.__dict__)
