#!/usr/bin/python3
def uppercase(str):
    j = 0
    for i in str:
        if (ord(i) >= 97 and ord(i) <= 122 and j == 0):
            str = chr(ord(i) - 32) + str[1:]
        elif (ord(i) >= 97 and ord(i) <= 122 and j > 0 and j < len(str) - 1):
            str = str[:j] + chr(ord(i) - 32) + str[j + 1:]
        elif (ord(i) >= 97 and ord(i) <= 122 and j == len(str) - 1):
            str = str[:j] + chr(ord(i) - 32)
        j = j + 1
    print(str)
