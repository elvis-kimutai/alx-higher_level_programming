#!/usr/bin/python3
"""Defines a function Python class-to-json"""


def class_to_json(obj):
    """Return the dictionary represntation of  data structure."""
    return obj.__dict__
