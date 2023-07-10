#!/usr/bin/python3
"""
    define a function inherits_from
"""


def inherits_from(obj, a_class):
    """
        check if an object is an inherited instance of a class
        Return: - True.
                - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
