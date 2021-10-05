#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i in new_list:
        try:
            i = new_list.index(search)
        except:
            return new_list
        new_list[i] = replace
    return new_list
