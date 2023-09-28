#!/usr/bin/python3
"""
    Defines peak-finding algorithm.
"""

def find_peak(list_of_integers):
    """finds the peak of a list"""
    list_len = len(list_of_integers)

    left = 0
    right = list_len - 1

    if list_len == 0:
        return None

    while (left < right):

        mid = (left + right) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
