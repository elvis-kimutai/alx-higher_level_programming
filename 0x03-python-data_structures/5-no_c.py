#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for e in my_string:
        if e not in ["c", "C"]:
            new = new + e
    return new
