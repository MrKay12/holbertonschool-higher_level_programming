#!/usr/bin/python3
def print_last_digit(num):
    if num < 0:
        num = (num * -1) % 10
    else:
        num = num % 10
    print(num, end="")
    return (num)
