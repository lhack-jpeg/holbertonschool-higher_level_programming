#!/usr/bin/python3
'''Create class rectangle'''


class Rectangle:
    '''Creates a rectangle object'''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''Initialisation of object. Runs check to ensure value passed
        are good.'''
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        '''Return width of object.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set width of object.'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Return Height of object.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set value of height of object.'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Returns the area of the object.'''
        return self.height * self.width

    def perimeter(self):
        '''Returns to perimeter of object. If height or width = 0
        perimeter is 0'''
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height * 2) + (self.width * 2)

    def __str__(self):
        '''Print out the rectangle using the # character
        if width or height is 0 return empty string'''
        if self.height == 0 or self.width == 0:
            return ""

        rect_string = ""
        for i in range(self.height):
            for j in range(self.width):
                rect_string += str(self.print_symbol)
            if i != self.height - 1:
                rect_string += "\n"
        return rect_string

    def __repr__(self):
        '''Returns a string of representation to recreate
        a new class'''
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        '''Delete object'''
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Compares two rectangles and returns the larger one.'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        '''Returns a new rectangle with width == height == size.'''
        return cls(size, size)
