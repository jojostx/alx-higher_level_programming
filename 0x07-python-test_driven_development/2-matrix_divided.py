#!/usr/bin/python3
"""
This module is composed of a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """ Function that divides all elements of a matrix
    Args:
        matrix: list of lists of integers or floats
        b: number (integer or float)
    Returns:
        A new matrix
    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats
        TypeError: If each row of the matrix is not of the same size
        TypeError: If div is not a number
        ZeroDivisionError: If div is 0
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not matrix or not isinstance(matrix, list):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    inner_len = -1
    new_m = matrix.copy()

    for inner_m in new_m:
        if not inner_m or not isinstance(inner_m, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

        for i, n in enumerate(inner_m):
            m_len = len(inner_m)

            if (inner_len == -1):
                inner_len = m_len

            if (m_len == 0) or (inner_len == -1) or (inner_len != m_len):
                raise TypeError(
                    "Each row of the matrix must have the same size")

            if type(n) not in [int, float]:
                raise TypeError(
                    ('matrix must be a matrix '
                        '(list of lists) of integers/floats'))

            # divide and replace
            inner_m[i] = round(n / div, 2)

    return new_m
