#!/usr/bin/python3
def uppercase(str):
    length = len(str)
    for i in range(0, length):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            print('{}'.format(chr(ord(str[i]) - 32)), end='')
        else:
            print('{}'.format(str[i]))
