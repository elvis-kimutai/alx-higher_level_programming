#!/usr/bin/python3
import sys


if __name__ == "__main__":
    l = sys.argv[1:]
    total = 0
    for k in l:
        total = total + int(k)
    print(total)
