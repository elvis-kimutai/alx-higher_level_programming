#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    e = list(tuple_a)
    k = list(tuple_b)

    while len(e) < 2:
        e.append(0)
    while len(k) < 2:
        k.append(0)

    e = e[:2]
    k = k[:2]
    return (e[0] + k[0], e[1] + k[1])
