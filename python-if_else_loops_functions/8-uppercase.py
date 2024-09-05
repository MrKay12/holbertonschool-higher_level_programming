#!/usr/bin/python3
def uppercase(str):
    anw = ""
    for char in str:
        if 'a' <= char <= 'z':
            anw += chr(ord(char) - 32)
        else:
            anw += char
    print("{:s}".format(anw))
