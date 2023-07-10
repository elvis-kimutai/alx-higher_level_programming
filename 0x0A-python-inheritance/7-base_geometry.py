#!/usr/bin/python3
"""
     define a class BaseGeometry
"""


class BaseGeometry:
    """
        Representation of class BaseGeometry
    """

    def area(self):
        """
        Raises the Exception with message
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
            validates the value as a positive integer
        """

        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
