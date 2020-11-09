#!/usr/bin/env python3

'''
module that logs date time according format YY-mm-dd HH:MM:SS
'''
__author__ = "fennaf"

## CODE
# Imports
import sys
import datetime

def main(args):
    #prepare
    # open logfile for append
    f = open('log.txt', 'a')
    d = datetime.datetime.now()
    f.write('{:%Y-%m-%d %H:%M:%S} {}'.format(d, '\n'))
    f.close()
    return 0

if __name__ == "__main__":
    exitcode = main(sys.argv)
    sys.exit(exitcode)
