#!usr/bin/#!/usr/bin/env python3

"""
This program generates a random dna string, computes the frequencies per base
and write the string and frequencies to an output file

usage : dna_gen <number>
example output:

Base frequencies of sequence: CGGACAGGCCTAGCT
A: 0.20 T: 0.13 G: 0.33 C: 0.33
"""


__author__ = "fennaf"

import sys
import random

def gen_dna(N):
    """generate dna based on random number N"""
    valid_dna = list('ATGC')
    dna = [random.choice(valid_dna) for i in range(N)]
    return ''.join(dna)


def get_base_frequencies(dna):
    """compute the frequency for each base"""
    return {base: dna.count(base)/float(len(dna))
                for base in 'ATGC'}


def format_frequencies(frequencies):
    """ format the frequencies to readable format into one string"""
    return "".join(['{}: {:.2f} '.format(base,frequencies[base])
        for base in frequencies])


def main(args):
    """ generate a random dna string, compute frequencies and write to file"""
    dna = gen_dna(int(args[1]))
    frequencies = get_base_frequencies(dna)
    formatted_freq = format_frequencies(frequencies)
    with open('output', 'w') as f:
        f.write('Base frequencies of sequence: {} \n'.format(dna))
        f.write(formatted_freq + '\n')

if __name__ == "__main__":
    exitcode = main(sys.argv)
    sys.exit(exitcode)
