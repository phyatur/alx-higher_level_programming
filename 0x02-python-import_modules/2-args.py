#!/usr/bin/python3
import sys
if __name__ == "__main__":
    length = len(sys.argv)
    if length > 1:
        if length == 2:
            print('{} argument:'.format(length-1))
            print('{}: {}'.format(1, sys.argv[1]))
            sys.exit()
        print('{} arguments:'.format(length-1))
        for i in range(1, length):
            print('{}: {}'.format(i, sys.argv[i]))
    elif length <= 1:
        print('{} arguments{}'.format(length - 1, '.'))
