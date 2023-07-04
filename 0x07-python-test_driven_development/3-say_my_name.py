#!/usr/bin/python3
"""
    Define function say_my_name.
"""


def say_my_name(first_name, last_name=""):
    """
        Print a Name
        Args:
            First_name (str): first name to print.
            Last_name (str): last name to print.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
