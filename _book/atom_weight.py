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
def calc_weight(element):
    if element in ATOMMASS:
        return ATOMMASS[element]
    print('Element not in mass table:', element)
    return 0


def processfile(input_file_name):
    f = open(input_file_name)
    count = 0
    for line in f:
        if line.startswith('ATOM') or line.startswith('HETATM'):
            atom = line[13:14]
            count += calc_weight(atom)
    f.close()
    return count


def store_atomweight(weight, output_file_name):
    o = open(output_file_name, 'w')
    o.write('atomweight:' + str(weight) + '\n')
    o.close()


#MAIN
def main(args):
    # Preparation
    if len(args) < 3:
        print("please provide the name of an input and an output file")
        print("Program stopping...")
        return 1
    input_file_name = args[1]
    output_file_name = args[2]

    # Work
    y = processfile(input_file_name)

    # Finalize
    store_atomweight(y, output_file_name)
    return 0


if __name__ == "__main__":
    exitcode = main(sys.argv)
    sys.exit(exitcode)
