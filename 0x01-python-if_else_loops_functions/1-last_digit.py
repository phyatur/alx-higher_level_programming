#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_number = number % 10
else:
    last_number = (abs(number) % 10) * -1

output = 'Last digit of {} is {} and is'

if last_number > 5:
    print((output + ' greater than 5').format(number, last_number))
elif last_number == 0:
    print((output + ' 0').format(number, last_number))
elif last_number < 6 and last_number != 0:
    print((output + ' less than 6 and not 0').format(number, last_number))
