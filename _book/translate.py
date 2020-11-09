#!/usr/bin/env python3

""" translates all protein files to nucleotide files (which is nonsense)
    usage: translate.py <inputfile>
"""

__author__ = 'fennaf'

#imports
import sys


def fetch_sequence(file):
    """ extract the sequence from a file"""
    sequence = ""
    f = open(file)
    for line in f:
        if not line.startswith('>'):
            sequence += line
    return sequence


def translate_aa2dna(aa_sequence):
    """ translate the aa sequence to dna sequence """
    dna_sequence = ""
    reverse_codon = {
        "A": "GCG", "C": "TGC", "D": "GAT", "E": "GAG",
        "F": "TTT", "G": "GGC", "H": "CAC", "I": "ATT",
        "K": "AAA", "L": "CTC", "M": "ATG", "N": "AAC",
        "P": "CCT", "Q": "CAA", "R": "CGC", "S": "TCG",
        "T": "ACA", "V": "GTC", "W": "TGG", "Y": "TAC",
        "*": "TAA",
    }
    for char in aa_sequence:
        if char in reverse_codon:
            dna_sequence += reverse_codon[char]
    return dna_sequence


def store_translation(output_file, sequence):
    """ stores the dna sequence """"
    print("store stranslation")
    o = open(output_file, "w")
    o.write(sequence)
    o.close()


def main(args):
    """ main function """
    files = args[1:]
    if len(files) < 1:
        print("please enter a file")
    else:
        for input_file in files:
            aa_sequence = fetch_sequence(input_file)
            dna_sequence = translate_aa2dna(aa_sequence)
            output_file = "output" + input_file[:-6]
            store_translation(output_file, dna_sequence)
    return 0


if __name__ == '__main__':
    exitcode = main(sys.argv)
    sys.exit(exitcode)
