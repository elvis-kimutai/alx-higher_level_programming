#!/usr/bin/python3
"""Defines a function from_json_string"""
import json


def from_json_string(my_str):
    """Return the Python object rep of a JSON string"""
    return json.loads(my_str)
