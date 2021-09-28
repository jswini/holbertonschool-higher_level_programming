#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
#Last digit of 4205 is 5 and is less than 6 and not 0
zero = "0"
greater_than_5 = "greater than 5"
less_than_6 = "less than 6 and not 0"
last_digit = number % 10
if last_digit > 5:
    print("Last digit of {} is {} and is {}".format(number, last_digit, greater_than_5))
elif last_digit == 0:
    print("Last digit of {} is {} and is {}".format(number, last_digit, zero))
else:
    print("Last digit of {} is {} and is {}".format(number, last_digit, less_than_6))
