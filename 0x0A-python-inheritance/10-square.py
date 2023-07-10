#!/usr/bin/python3
"""
    define a class Square that inherits from BaseGeometry
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Rep of Square
    """

    def __init__(self, size):
        """
            instantiate the private instance field size
        """

        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
