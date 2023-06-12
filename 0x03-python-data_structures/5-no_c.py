#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)
    for i in range(length):
        if my_string[i] == 'C' or my_string[i] == 'c':
            continue
        print('{}'.format(my_string[i]), end='')
    return ''
