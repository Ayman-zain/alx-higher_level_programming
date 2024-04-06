#!/usr/bin/python3
for i in range(0, 99):
    if (chr(i) != 'q' and chr(i) != 'e'):
        print("{} = {}".format(i, hex(i)))
