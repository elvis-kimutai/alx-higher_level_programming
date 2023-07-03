#!/usr/bin/python3
"""
    define a class Square
"""


class Rectangle:
    """
        A Rectangle with private instance attributes: width and height
    """

    def __init__(self, width=0, height=0):
        """
            Args:
                width (int): width of the new Rectangle
                height (int): height of the new Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            gets the width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            validate the width as a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            get the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            validate the height as a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            Return: area of the Rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
            Return: perimeter of Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """
            Return: printable representation of rectangle"#"
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
