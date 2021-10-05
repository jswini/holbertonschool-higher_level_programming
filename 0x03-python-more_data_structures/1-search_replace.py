#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_index = my_list.index(search)
    my_list[list_index] = replace
    return my_list
