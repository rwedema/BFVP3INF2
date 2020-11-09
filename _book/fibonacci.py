#!/usr/bin/env python3

"""
program hat prints out the Fibonacci sequence with a start point derived from the
maxval taken from the commandline, 10 numbers long, without printing the
second number from the range
    usage: fibonacc.py <maxval>
    example output maxval = 200: [2, '*', 5, 8, 13, 21, 34, 55, 89, 144]
"""

__author__ = "F.Feenstra, M.Kempenaar, T. Wassenaar"

## CODE

# Imports
import sys


# Constants
MINFIBO = 55


# Functions
def compose_fibonacci(maxval):
    """compose Fibonacci sequence till maximum"""
    fibo_seq = [0, 1]
    nextval = 0
    while nextval <= maxval:
        nextval = fibo_seq[-2] + fibo_seq[-1]
        fibo_seq.append(nextval)
    return fibo_seq


def cut_range(fibo_seq, length=10):
    """fetch range of length_seq numbers but do not return the 2nd number"""
    fibo = []
    for i in range(len(fibo_seq) - length, len(fibo_seq)):
        fibo.append(fibo_seq[i-1])
    fibo[1] = '*'
    return fibo


# Main
def main(args):
    """
    main function which fetches max from command line
    and prints a sequence of 10 numbers long (except 2nd number)
    """

    # Preparation
    maxval = int(args[1])
    if maxval < MINFIBO:
        print("your provided maximum is too low, please enter a higher number")
        return 1

    # Work
    fibo = compose_fibonacci(maxval)
    fibo = cut_range(fibo)

    # Finalize
    print(fibo)
    return 0


if __name__ == "__main__":
    exitcode = main(sys.argv)
    sys.exit(exitcode)
