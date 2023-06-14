#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_list = sorted(a_dictionary)
    for i in range(len(sort_list)):
        print('{}: {}'.format(sort_list[i], a_dictionary[sort_list[i]]))
