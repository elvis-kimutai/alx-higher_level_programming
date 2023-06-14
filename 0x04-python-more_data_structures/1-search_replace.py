#!/usr/bin/python3

def search_replace(my_list, search, replace):
    results = my_list.copy()
    for i in range(len(results)):
        if results[i] == search:
            results[i] = replace
    return results
