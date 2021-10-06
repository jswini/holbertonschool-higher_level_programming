def print_sorted_dictionary(a_dictionary):
    print(a_dictionary)
    my_dictionary = sorted(a_dictionary.keys())
    for i in my_dictionary:
        print("{}: {}".format(i, a_dictionary[i]))
