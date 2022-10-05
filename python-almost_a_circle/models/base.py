#!/usr/bin/python3
'''
This module contains the constructor for the base class
'''

import json


class Base():
    '''
    Constructor for base class
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Returns a JSON string of list dictionaries.'''
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Write JSON string to file.'''
        obj_list = []
        if list_objs is not None:
            for item in list_objs:
                obj_list.append(item.to_dictionary())

        filename = str(cls.__name__) + '.json'

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(obj_list))
