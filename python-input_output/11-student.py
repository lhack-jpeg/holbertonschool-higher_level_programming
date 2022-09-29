#!/usr/bin/python3
'''
This module contains the the class contstructor student.
'''


class Student():
    '''Student class constructor.'''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return (self.__dict__)
        else:
            stud_dict = dict()
            keys = list(set(attrs).intersection(vars(self).keys()))
            for key in keys:
                stud_dict[key] = vars(self).get(key)
            return stud_dict

    def reload_from_json(self, json):
        for key in json:
            try:
                setattr(self, key, json[key])
            except Exception as e:
                pass
