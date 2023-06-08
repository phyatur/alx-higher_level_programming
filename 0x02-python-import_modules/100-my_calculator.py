#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    operator = argv[2]
    first = int(argv[1])
    second = int(argv[3])

    if operator == '+':
        result = add(first, second)

    elif operator == '-':
        result = sub(first, second)

    elif operator == '*':
        result = mul(first, second)

    elif operator == '/':
        result = div(first, second)

    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    print('{} {} {} = {}'.format(first, operator, second, result))
