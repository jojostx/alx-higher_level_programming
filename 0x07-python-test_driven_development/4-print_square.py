#!/usr/bin/python3
"""
This module is composed of a function that prints a square with the character '#'
"""


def print_square(size):
    """ Function that prints a square with the character #
    Args:
        size: the size length of the square
    Returns:
        No return
    Raises:
        TypeError: If size is a float and is less than 0
        TypeError: If size isn't an integer
        ValueError: If size is less than 0
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for n in range(size):
        print(f"{'#' * size}")
