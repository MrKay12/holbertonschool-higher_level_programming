#!/usr/bin/python3
from sys import argv
i = 1
sum = 0
argc = len(argv)
if __name__ == "__main__":
    while i < argc:
        sum += int(argv[i])
        i += 1
    print("{}".format(sum))
