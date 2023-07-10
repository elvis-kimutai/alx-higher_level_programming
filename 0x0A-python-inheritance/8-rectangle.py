#!/usr/bin/python3
"""
    defines a class Rectangle inheriting from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        rep of Rectangle
    """

    def __init__(self, width, height):
        """
            intialize new Rectangle
            Args:
                width (int): width of new rectangle
                height (int): height of  new rectangle
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
