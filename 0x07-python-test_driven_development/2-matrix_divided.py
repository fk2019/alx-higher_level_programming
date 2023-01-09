#!/usr/bin/python3
"""This module defines a matrix_divided function

Args:
    matrix: matrix(list of lists)
    div: divisor

Raises:
    TypeError: matrix must be a matrix (list of lists) of integers/floats
    TypeError: div must be a number
    TypeError: Each row of the matrix must have the same size
    ZeroDivisionError: division by zero
"""


def matrix_divided(matrix, div):
    """Divides matrix by div and return a new matrix"""
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    size = None
    for i in matrix:
        if type(i) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(i)
        elif size != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")
            if type(int(j)) is not int:
                raise ValueErrror("cannot convert float NaN to integer")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(int(div)) is not int:
        raise ValueError("cannot convert float float NaN to integer")

    return [[round(i / div, 2) for i in j] for j in matrix]
