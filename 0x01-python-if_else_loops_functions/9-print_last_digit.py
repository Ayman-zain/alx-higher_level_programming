#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        number = number * -1
    if (number < 10):
        print(number, end="")
        return number
    elif (number >= 10):
        number = number / 10
        frac = number % 1
        frac = int(frac * 10)
        print(frac, end="")
        return frac     
