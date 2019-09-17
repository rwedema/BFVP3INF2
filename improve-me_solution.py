#!/usr/bin/env python3

# ASSIGNMENT a. # Write docstring for the program *and* for every functie
""" Program that prints all pairs of consecutive amino acids from pdb file"""

import sys


AMINOACIDS = "A   R   N   D   C   E   Q   G   H   I   L   K   M   F   P   S   T   W   Y   V".split()
THREELETTR = "ALA ARG ASN ASP CYS GLU GLN GLY HIS ILE LEU LYS MET PHE PRO SER THR TRP TYR VAL".split()
PERCENTAGE = "7.4 4.2 4.4 5.9 3.3 5.8 3.7 7.4 2.9 3.8 7.6 7.2 1.8 4.0 5.0 8.1 6.2 1.3 3.3 6.8".split()


# ASSIGNMENT b. # rewrite one of the following loops to a dict comprehension
#d = {key: value for (key, value) in iterable}
AMINO321 = {aa3: aa1 for (aa3, aa1) in zip(THREELETTR, AMINOACIDS)}
#AMINO321 = {}
#for aa3, aa1 in zip(THREELETTR, AMINOACIDS):
#    AMINO321[aa3] = aa1

FREQUENCY = {aa1:float(perc)/100 for (aa1, perc) in zip(AMINOACIDS, PERCENTAGE)}
#FREQUENCY = {}
#for aa1, perc in zip(AMINOACIDS, PERCENTAGE):
#    FREQUENCY[aa1] = float(perc)/100


def is_calpha_atom(pdbline):
    return pdbline.startswith('ATOM') and pdbline[13:15] == 'CA'


def read_calpha_atoms(pdbfile):
    with open(pdbfile) as pdb:
        calpha_list = []
        # ASSIGNMENT c. # REWRITE THE FOLLOWING LOOP TO A LIST COMPREHENSION
        calpha_list = [AMINO321[line[17:20]] for line in pdb if is_calpha_atom(line)]
        #for line in pdb:
            #if is_calpha_atom(line):
                #calpha_list.append(AMINO321[line[17:20]])
    return calpha_list


def process(pdbfile):

    sequence = read_calpha_atoms(pdbfile)

    # Generate all pairs of consecutive amino acids
    pairs = list(zip(sequence, sequence[1:]))
    count = len(pairs)

    # Calculate how often a pair is expected, based on frequency and count
    expected = [ [ FREQUENCY[i]*FREQUENCY[j]*count for i in AMINOACIDS ] for j in AMINOACIDS ]

    # Count the pairs
    observed = [ [ pairs.count((i, j)) for i in AMINOACIDS ] for j in AMINOACIDS ]

    # Print a table of the pairs

    # ASSIGNMENT c. # Use string formatting to print a nice table of results here,
    #               # rounding numbers at one decimal
    for i in AMINOACIDS:
        print("{1:>5s}".format(5,i), end = "")
    print()
    for aa, expect, observ in zip(AMINOACIDS, expected, observed):
        print("{} ".format(aa), end="")
        for exp, obs in zip(expect, observ):
            print("{: .1f}".format(obs - exp), end=" ")
        print()

    return


## MAIN
def main(args):
    pdbfile = args[1]
    process(pdbfile)
    return 0


# -- not giving away the final clause, sorry...
main(sys.argv)
