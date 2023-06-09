#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    length = len(roman_string)
    sum = 0
    numerals = {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000}
    for i in roman_string:
        for j in numerals:
            if i == numerals[j]:
                sum += numerals[j]
    return sum
