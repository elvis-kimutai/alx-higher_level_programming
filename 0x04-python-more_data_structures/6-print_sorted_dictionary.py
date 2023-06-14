#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_ = sorted(a_dictionary)
    for key in sorted_:
        print(key + ":", a_dictionary[key])
