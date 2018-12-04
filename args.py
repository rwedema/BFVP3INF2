#!usr/bin/#!/usr/bin/env python3

__author__ = "fennaf"

import sys


def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)

def main():
    multiply(4, 5)
    multiply(10, 9)
    multiply(2, 3, 4)
    multiply(3, 5, 10, 6)
    # one can use * to unpack as well
    test = (4,5,6,)
    multiply(*test)

if __name__ == '__main__':
    exitcode = main()
    sys.exit(exitcode)
