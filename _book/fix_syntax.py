#!/usr/bin/env python3

""" # 01: needed a quote
A silly program with a collection of syntax errors
"""

__author__ = "Tsjerk A. Wassenaar" #08 insert =


# IMPORTS
import sys #02: remove ':'


# CONSTANTS
two_times_pi = 6.283185 #10 two instead of 2
mass = {
    "H": 1.008, #09 , instead of ;
    "C": 12.011,
    "O": 15.998,
    } #03: remove '}'


# FUNCTIONS
#def 04: remove def

def fun(a, b, c): #05 added :
    return ( ((a) + (b)) * c) #06 wrong parenthis order


# MAIN
def main(args):
    print(fun(mass['H'], mass['C'], mass['O']))
    return 0


if __name__ == "__main__": #06 == instead of =
    exitcode = main(sys.argv) # 07 sys.argv instead of sys..argv
    sys.exit(exitcode) #11
