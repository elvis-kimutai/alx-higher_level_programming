#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    Max = my_list[0]
    for e in my_list:
        if h > Max:
            Max = e
    return Max
