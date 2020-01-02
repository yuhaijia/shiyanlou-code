#! /usr/bin/env python3

import sys

def Hours(min):
    h = min // 60
    m = min % 60
    print("{} H, {} M".format(h, m))

try:
    if (int(sys.argv[-1]) < 0) or sys.argv[-1][-1].isalpha():
        raise ValueError
    else:
        min = int(sys.argv[-1])
        Hours(min)
except ValueError:
    print("Parameter Error. Please enter a positive number for minutes!")
