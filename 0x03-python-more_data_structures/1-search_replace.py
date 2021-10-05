#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_index = my_list.index(search)
    new_list = my_list.copy()
    new_list[list_index] = replace
    return new_list
