#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    length = len(argv) - 1
    if length == 0:
        print("{} arguments.". format(length))
    elif n == 1:
        print("{} argument:".format(length))
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(length))
        i = 1
        for arg in argv[1:]:
            print("{}: {}".format(i, arg))
            i += 1
