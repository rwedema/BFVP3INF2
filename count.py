#!/usr/bin/env python3

"""this programme reads fasta file(s) and reports number of nucleotides/amino acids"""


# METADATA VARIABLES
__author__ = "fennaf"
__version__ = "2018"

# IMPORTS
import sys

# LOGICA

def fetch_sequence(file):
    """ extract the sequence from a file"""
    sequence = ""
    f = open(file)
    for line in f:
        if not line.startswith('>'):
            sequence += line
    return sequence


def count_ATCG(sequence):
    A = sequence.count('A')
    C = sequence.count('C')
    T = sequence.count('T')
    G = sequence.count('G')
    return [A, C, T, G]

def count_cg(sequence):
    """count cg percentage"""
    gc = sequence.count('G') + sequence.count('C')
    return gc / len(sequence)


def determine_type(sequence):
    """distinghuis file types"""
    if sequence[0] == 'M':
        file_type = "protein_fasta"
    else:
        file_type = "nucleotide_fasta"
    # here you have to come up with a solution to distinghuis file types.
    return file_type


def main(args):
    #preperation
    filenames = args[1:]
    #work
    for file in filenames:
        sequence = fetch_sequence(file)
        file_type = determine_type(sequence)
        length = len(sequence)
        if file_type == "nucleotide_fasta":
            [A, T, G, C] = count_ATCG(sequence)
            cg = count_cg(sequence)
    #finish
    print('filetype: {}'.format(file_type))
    if file_type == "nucleotide_fasta":
        print('#nucleotides: {}'.format(length))
        print('#A:{}, #C:{}, #G:{}, #T:{}, '.format(A,T,G,C))
        print('CG percentage: {:.2%}'.format(cg))
    else:
        print('#amino acids: {}'.format(length))
    return 0

if __name__ == '__main__':
    exitcode= main(sys.argv)
    sys.exit(exitcode)
