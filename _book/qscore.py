#!/usr/bin/env python3

"""
This is a program that calculates
- Phredscore (Ascii value - 33)
- Accuracy: (exponent =(-1*numscore/10); Q = 1 - (10**exponent))

input: a file with reads from a sequencer (default reads.fq)
Each read constists of:

A first line describing the machine it was run on, the chip identifier and
-the actual coordinates from the chip where the base was read :@M01785:20:0...
-The actual read sequence                    :NTCATGTACGGTCAGGATGG...
-The plus sign                               :+
-The predicted read base quality ASCII value :#>>1A1B3B11BAEFFBECA...

The purpose is to read the line with the quality ASCII values (line after +)
and calculates Phredscore and quality base

The outcome of the test string #>>1A1B3B1 should be:

Quality score: #>>1A1B3B1
Phredscore   :    2    |   29   |   29   |   16   |   32   |   16   |   33   |   18   |   33   |   16   |
Accuracy     :  36.90% | 99.87% | 99.87% | 97.49% | 99.94% | 97.49% | 99.95% | 98.42% | 99.95% | 97.49% |

"""

__author__ = 'your name'


#imports
import sys


def main(args):
    return 0

#entryppoint
if __name__ == '__main__':
    exitcode = main(sys.argv)
    sys.exit(exitcode)
