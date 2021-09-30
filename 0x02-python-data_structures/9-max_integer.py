#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    my_list.sort()
    return my_list[length - 1]
