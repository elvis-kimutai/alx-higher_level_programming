#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    Rom_numeral = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
            }
    results = 0
    valueprev = 0

    for _numeral in reversed(roman_string):
        present_val = Rom_numeral.get(_numeral, 0)

        if present_val >= valueprev:
            results = results + present_val
        else:
            results = results - present_val
        valueprev = present_val
    return results
