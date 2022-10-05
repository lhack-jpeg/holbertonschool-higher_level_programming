#!/usr/bin/python3
'''
This module contains the class constructor for the square class.
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''Class constructor.'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Class initialisation method, using Rectangle to set attributes.'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''
        The string method to return a formatted string describing the
        instance.
        '''
        return (f'[{type(self).__name__}] ({self.id}) \
{self.x}/{self.y} - {self.width}')

    @property
    def size(self):
        '''Getter method for size attribute.'''
        return self.width

    @size.setter
    def size(self, value):
        '''Setter method of height, width.'''
        try:
            self.integer_validator("width", value)
            self.width = value
            self.height = value
        except Exception as e:
            raise e

    def update(self, *args, **kwargs):
        '''
        This method updates the value for the instance using
        either *args or **kwargs.
        '''
        if args is not None and len(args) > 0:
            attr_tuple = ('id', 'size', 'x', 'y')
            for x in range(len(args)):
                setattr(self, attr_tuple[x], args[x])
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, str(key), value)

    def to_dictionary(self):
        new_dict = super().to_dictionary()
        new_dict['size'] = new_dict.pop('width')
        new_dict.pop('height')
        return new_dict
