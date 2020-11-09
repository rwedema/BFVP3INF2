#!/usr/bin/#!/usr/bin/env python3

"""Analyses The GC content per gene.
   Conditions:
   1. Use a dna.py to import. The dna.py should have a function to calculate the CG content.
   2. Use functions. Use keywords arguments instead of conditional arguments
   3. Use NC_012655.ffn as a default but make the program flexible for other genome files.

   usage: gcpercentage <inputfile> <outputfile>
   """

__author__ = 'fenna'

#imports
import sys
import DNA


#functions
def get_geneID(header):
    """fetches the unique id from header"""
    geneID = header[31:43].replace('B',' ').replace('ac', '  ')
    return geneID


def process_gene(header, gene):
    """ process a line with iD, ,length of gene and gc percentage """
    ID = get_geneID(header=header)
    GC = DNA.gc(gene)
    gline = '{} {:4d} {:.2%} {}'.format(ID, len(gene), GC/100, '\n')
    return gline


def process_file(input_file = 'NC_012655.ffn',output_file = 'NC_012655.output'):
    """ processes the file line by line """
    #prepare
    f = open(input_file, 'r')
    o = open(output_file,'w')
    seq = ''
    header = f.readline()
    o.write('GeneID      Length    GC \n')
    #work
    for line in f:
        if not line.startswith('>'):
            seq += line
        else:
            o.write(process_gene(header = header, gene = seq))
            header = line
            seq = ''
    #finish
    f.close()
    o.close()
    return 0


def main(args):
    """ main function """
    if len(args) == 3:
        process_file(input_file=args[1],output_file=args[2])
    else:
        process_file()
    return 0


if __name__ == '__main__':
    exitcode = main(sys.argv)
    sys.exit(exitcode)
