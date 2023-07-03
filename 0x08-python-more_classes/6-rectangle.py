#!/usr/bin/python3
"""
    define a class Rectangle
"""


class Rectangle:
    """
        Rectangle with private instance attributes: width and height
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
            Args:
                width (int): width of the new rectangle
                height (int): height of the new rectangle
        """
        Rectangle.number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
            get the width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            validate the width as a positive integer
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
            gets the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            validates the height as a positive integer
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
            Return: Area of the Rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
            Return: Perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
            Return: printable representation of rectangle(#)
        """
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        for i in range(self.height):
            string += "#" * self.width
            if i < self.height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """
            Return: string representation of rectangle(#)
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """
            prints message when a rectangle is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
