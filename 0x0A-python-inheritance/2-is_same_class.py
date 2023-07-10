#!/usr/bin/python3
"""
    define a class is_same_class
"""


def is_same_class(obj, a_class):
    """
        check if an object is an exact instance of the specified class
        Return: - True
                - False
    """
    if type(obj) == a_class:
        return True
    return False
