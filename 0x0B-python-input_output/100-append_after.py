#!/usr/bin/python3
"""Define function append_after """


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line """
    text = ""
    with open(filename) as f:
        for line in f:
            text = text + line
            if search_string in line:
                text = text + new_string

    with open(filename, "w") as k:
        k.write(text)
