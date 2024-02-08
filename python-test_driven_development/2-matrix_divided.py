#!/usr/bin/python3

"""
module documentation
"""


def matrix_divided(matrix, div):
    """
    function documentation
    """
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not all(isinstance(element, (int, float))
               for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list\
of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return new_matrix
