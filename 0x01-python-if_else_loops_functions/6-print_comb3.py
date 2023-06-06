#!/usr/bin/python3
for x in range(0, 10):
    for y in range(x+1, 10):
        print("{:d}".format(x), end='')
        if x == 8 and y == 9:
            print("{:d}".format(y), end='\n')
        else:
            print("{:d}".format(y), end=', ')
