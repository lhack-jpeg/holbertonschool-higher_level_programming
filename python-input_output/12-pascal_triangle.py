#!/usr/bin/python3
'''
This module contains the function to return a pascal triangle.
'''


def pascal_recur(pascal_tri, n):
    if n == 1:
        return pascal_tri

    prev_row = pascal_tri[-1]
    prev_row_len = len(prev_row)
    row = [1, 1]
    for x in range(0, prev_row_len):
        try:
            row.insert(x + 1, prev_row[x] + prev_row[x + 1])
        except IndexError:
            pass

    pascal_tri.append(row)
    return pascal_recur(pascal_tri, n - 1)

def pascal_triangle(n):
    '''Function to return a pascal triangle.'''
    pascal_tri = []
    if n <= 0:
        return pascal_tri
    pascal_tri = [[1,1]]
    return pascal_recur(pascal_tri, n - 1)
