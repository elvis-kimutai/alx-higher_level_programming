#!/usr/bin/python3
"""
    defines a function add_attribute
"""


def add_attribute(obj, nam, value):
    """
        adds a new attribute to an object if possible
    """

    if hasattr(obj, '__dict__'):
        setattr(obj, nam, value)
    else:
        raise TypeError('can\'t add new attribute')
