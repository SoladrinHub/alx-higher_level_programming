#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        print("{}".format(i))
    else:
        print("{0:02}".format(i), end=", ")
