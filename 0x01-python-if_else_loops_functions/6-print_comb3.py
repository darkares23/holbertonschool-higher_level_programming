#!/usr/bin/python3
for i in range(0, 10):
    for h in range(0, 10):
        if i < h and i != 8:
            print("{}{}".format(i, h), end=', ')
        elif h > i:
            print("{}{}".format(i, h))
