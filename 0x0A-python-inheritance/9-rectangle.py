#!/usr/bin/python3
"""
    Define a class Rectangle that inherit from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Representation of Rectangle
    """

    def __init__(self, width, height):
        """
            intialize a new 'Rectangle'
            Args:
                width: width of the new rectangle
                heigh: height of the new rectangle
        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
            Return: The area of the rectangle
        """

        return self.__width * self.__height

    def __str__(self):
        """
            Return: print() & str() representation of a Rectangle
        """

        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
