#!/usr/bin/python3
"""
    define a class MyList
"""


class MyList(list):
    """
        Implements sorted list
    """

    def print_sorted(self):
        """
            print sorted list
        """
        print(sorted(self))
