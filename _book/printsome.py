#!/usr/bin/env python3
"""this programme prints the filename"""

__author__ = "fennaf"

import sys

def main(args):
    filenames = args[1:]
    for file in filenames:
        print('filename: {}'.format(file))
    return 0

if __name__ == '__main__':
    exitcode= main(sys.argv)
    sys.exit(exitcode)
