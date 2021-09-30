#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    if len(a) == 1:
        a.append(0)
    elif len(a) == 0:
        a = [0, 0]
    b = list(tuple_b)
    if len(b) == 1:
        b.append(0)
    elif len(b) == 0:
        b = [0, 0]
    c = []
    for i in range(2):
        c.append(a[i] + b[i])
    return ("({}, {})".format(c[0], c[1]))
