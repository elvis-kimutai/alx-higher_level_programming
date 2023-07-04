#!/usr/bin/python3
"""
    Define function print_square.
"""


def print_square(size):
    """
        Print a square with the # character
        Args: Size (int): height/width of the square.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
