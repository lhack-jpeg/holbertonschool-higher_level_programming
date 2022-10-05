#!/usr/bin/python3
'''
This module contains the constructor for the base class
'''

import json
from os.path import exists


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
        """ returns a json string of a dictionary """
        if not list_dictionaries or list_dictionaries == '':
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Class method to save lists of instances to file.'''
        obj_list = []
        if list_objs is not None:
            for obj in list_objs:
                obj_list.append(obj.to_dictionary())

        json_string = cls.to_json_string(obj_list)
        filename = cls.__name__ + '.json'

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Method to return rectangle or square instances using the base
        class.'''
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        if cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''Returns a list of class instances.'''
        filename = cls.__name__ + '.json'
        if not exists(filename):
            return []
        with open(filename, 'r', encoding='utf-8') as f:
            obj_data = cls.from_json_string(f.read())
            class_list = []
            for obj in obj_data:
                class_list.append(cls.create(**obj))
            return class_list
