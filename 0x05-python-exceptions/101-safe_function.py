#!/usr/bin/python3
# executes a function safely.

import sys


def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as error:
        sys.stderr.write("Exception: {}\n".format(error))
        return None
