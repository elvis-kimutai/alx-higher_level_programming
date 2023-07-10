#!/usr/bin/python3
"""
    define a class MyInt that inherits from int.
"""


class MyInt(int):
    """
        inverts int operators == and !=
    """

    def __eq__(self, val):
        """
            overrides  =  opeartor with !=
        """

        return self.real != val

    def __ne__(self, val):
        """
            override != operator with ==
        """

        return self.real == val
