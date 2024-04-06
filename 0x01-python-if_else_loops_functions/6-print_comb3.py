#!/usr/bin/python3
for i in range(1, 100):
    if (i < 10):
        print("0{}".format(i), end=", ")
    elif (i // 10 < i % 10):
        print("{}".format(i), end=", " if i < 89 else "\n")
