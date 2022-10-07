#!/usr/bin/python3
'''
This module contains the constructor for the base class
'''

import json
from os.path import exists
import csv


class Base():
    '''
    Constructor for base class
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Initialisation of the instance.'''
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
        '''Returns a list of objects.'''
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Saves list of object instances to file.'''
        filename = cls.__name__ + '.csv'
        if cls.__name__ == 'Square':
            fieldnames = ['id', 'size', 'x', 'y']
        else:
            fieldnames = ['id', 'width', 'height', 'x', 'y']
        obj_list= []
        if list_objs is not None:
            for obj in list_objs:
                obj_list.append(obj.to_dictionary())
        with open(filename, 'w', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for obj in obj_list:
                writer.writerow(obj)

    @classmethod
    def load_from_file_csv(cls):
        '''Returns a list of class instances.'''
        filename = cls.__name__ + '.csv'
        if not exists(filename):
            return []
        dict_list = []
        if cls.__name__ == 'Square':
            fieldnames = ['id', 'size', 'x', 'y']
        else:
            fieldnames = ['id', 'width', 'height', 'x', 'y']
        try:
            with open(filename, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile, fieldnames=fieldnames)
                for row in reader:
                    row = {key: int(value) for key, value in row.items()}
                    dict_list.append(cls.create(**row))
                return dict_list
        except Exception:
            return dict_list
            


