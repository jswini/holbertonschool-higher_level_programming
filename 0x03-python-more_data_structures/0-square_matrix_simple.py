#!/usr/bin/python3
'''
Prototype: def square_matrix_simple(matrix=[]):
matrix is a 2 dimensional array
Returns a new matrix:
Same size as matrix
Each value should be the square of the value of the input
Initial matrix should not be modified
You are not allowed to import any module
You are allowed to use regular loops, map, etc.
'''
def square_matrix_simple(matrix=[]):
    new_matrix = [[]]
    for i in matrix:
        new_matrix.append(list(map(lambda x : x ** 2, i)))
    return new_matrix
