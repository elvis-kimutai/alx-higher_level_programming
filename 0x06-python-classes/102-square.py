#!/usr/bin/python3
"""
    define a class Square
"""

class Square:
    """
        square with private instance attribute: size
    """

    def __init__(self, size=0):
        """
            Args:
                size (int): size of the new square
        """
        self.size = size

    @property
    def size(self):
        """
            gets the current size of the square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
            validate the size is an integer that is greater than zero
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
            Return: The area of the square
        """
        return (self.__size * self.__size)

    def __eq__(self, other):
        """
            defines == comparision to a square
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
            defines != comparison to a square
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
            defines < comparison to a square
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
            defines <= comparison to a square
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
            defines > comparison to a square
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
            defines >= compmarison to a square
        """
        return self.area() >= other.area()
