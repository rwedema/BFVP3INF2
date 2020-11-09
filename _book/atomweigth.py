#!/usr/bin/env python3

"""
This program takes a pdb file and calculates the atomweigth
"""

__author__ = "F.Feenstra, M.Kempenaar, T. Wassenaar"

#IMPORTS
import sys


#CONSTANTS
# Atom masses don't change...
ATOMMASS = {
    'C': 12.011,
    'N': 14.007,
    'O': 15.998,
    'P': 30.974,
    'S': 32.065,
    'H': 1.008
}


#FUNCTIONS
def calcWeight(atom):
    if element in ATOMMASS:
        return ATOMMASS[element]
    print('Element not in mass table:', element)
    return 0


def processfile(inputFileName):
    f = open(inputFileName)
    count = 0
    for line in f:
        if line.startswith('ATOM') or line.startswith('HETATM'):
            atom = line[13:14]
            count += calcWeight(atom)
    f.close()
    return count


def storeAtomweight(weight, outputFileName):
    o = open(outputFileName, 'w')
    o.write('atomweight:' + str(weight) + '\n')
    o.close()


#MAIN
def main(args):
    # Preparation
    if len(args) < 3:
        print("please provide the name of an input and an output file")
        print("Program stopping...")
        return 1
    inputFileName = args[1]
    outputFileName = args[2]

    # Work
    y = processfile(inputFileName)

    # Finalize
    storeAtomweight(y, outputFileName)
    return 0


if __name__ == "__main__":
    exitcode = main(sys.argv)
    sys.exit(exitcode)
