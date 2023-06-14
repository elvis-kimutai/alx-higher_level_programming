#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_del = []
    for k, v in a_dictionary.items():
        if v == value:
            key_del.append(k)
    for k in key_del:
        del a_dictionary[k]
    return a_dictionary
