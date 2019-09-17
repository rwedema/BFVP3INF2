#!/usr/bin/env python3
"""
Use list comprehensions and lambda functions to make the code work.
Do not use extra lines of code!!!
Note that this exercise is to demonstrate the working of list comprehensions and lambda functions.
Code readability is always more preferred over compact code
"""

__author__ = 'jurrehageman'

import sys

bases = {'A':'T','C':'G','G':'C','T':'A'}


def reverse(seq):
    rev = seq[::-1]
    return rev


def complement(seq):
    comp = ''.join([bases[i] for i in seq])
    return comp


def reverse_complement(seq):
    rev_comp = lambda x: "".join([bases[x] for x in seq][::-1])
    return rev_comp(seq)


def main():
    #dna = "ATCG"
    dna = input("provide sequence:(5'-3'): ").upper()
    rev_dna = reverse(dna)
    comp_dna = complement(dna)
    reverse_comp_dna = reverse_complement(dna)
    print("Input: 5'-{}-3'".format(dna))
    print("Reverse: 3'-{}-5'".format(rev_dna))
    print("Complement: 5'-{}-3'".format(comp_dna))
    print("Reverse Complement: 5'-{}-3'".format(reverse_comp_dna))

    return 0

if __name__ == '__main__':
    sys.exit(main())