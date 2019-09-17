#!/usr/bin python

"""
Align two sequences using Needleman-Wunsch or Smith-Waterman.

(c)2014 Tsjerk A. Wassenaar
        Hanze University of Applied Sciences
"""

import sys, numpy


# Amino acids
AA1   = "A   C   D   E   F   G   H   I   K   L   M   N   P   Q   R   S   T   V   W   Y".split()
AA    = dict((b, a) for a, b in enumerate(AA1))
AA3   = "ALA CYS ASP GLU PHE GLY HIS ILE LYS LEU MET ASN PRO GLN ARG SER THR VAL TRP TYR".split()
AA321 = dict(zip(AA3, AA1))
LA = len(AA)
RLA = range(len(AA))
pdb = None

# BLOSUM 50 matrix in condensed form
BLOSUM50=("""kdedeeefdedeecegfcdfa medbgfcfbcidcceececa mhdfffgcbfdbdgfbdca """
          """nbfheebbebaefeacba sccccddcddbeeacea mhdgcdhfbefeeeca """ #01
          """lcfbcgdceeecdca ndbbdcbdfdccba pbcfeededchba khchfcceceja """
          """kcigbcedega ldbefecdca mfcdeefga nbcdgjea peebcca khbdda kcdfa uhca nea ka g""")

# Unpacking - Magic.
BLOSUM50=[(len(AA)*[0]+[ord(i)-102 for i in list(j)])[-1-LA:] for j in BLOSUM50.split()]

# Symmetrizing
BLOSUM50=[[BLOSUM50[i][j] if i==j else BLOSUM50[i][j]+BLOSUM50[j][i] for j in RLA] for i in RLA]

# Text colors
RED = "\033[1;35;47m"
OFF = "\033[32;47m"


def align(seq1, seq2, blosum=BLOSUM50, penalty=-50, method="N"): #02
    """ Perform sequence alignment and return aligned objects. """

    s1 = [AA.get(i, len(AA)) for i in seq1]
    s2 = [AA.get(i, len(AA)) for i in seq2]

    m = len(seq1)
    n = len(seq2)

    M =  [(n+1)*[penalty] for i in range(m+1)]

    if method == "S":
        # Smith-Waterman
        M[0] = (n+1)*[0]
        for i in range(1,m+1):
            M[i][0] = 0
    else:
        # Needleman-Wunsch
        M[0] = [i*penalty for i in range(len(M[0]))]
        for i in range(1,m+1):
            M[i][0] = i*penalty

    for i in range(m):
        for j in range(n):
            match  = M[i][j] + blosum[s1[i]][s2[j]] #10
            delete = M[i][j+1] + penalty
            insert = M[i+1][j] + penalty
            M[i+1][j+1] = max(match, delete, insert)

    aln1, aln2 = [], []

    while m or n:
        if m and n and M[m][n] == M[m-1][n-1] + blosum[s1[m-1]][s2[n-1]]:
            aln1.append(seq1[m-1])
            aln2.append(seq2[n-1])
            m    -= 1
            n    -= 1
        elif m and M[m][n] == M[m-1][n] + penalty:
            aln1.append(seq1[m-1])
            aln2.append("-")
            m    -= 1
        elif n and M[m][n] == M[m][n-1] + penalty:
            aln1.append("-")
            aln2.append(seq2[n-1])
            n    -= 1
        else:
            # End of sequence. Wrap up and break out of loop.
            aln1.append(n*"-")
            aln1.extend(seq1[:m][::-1])
            aln2.append(m*"-")
            aln2.extend(seq2[:n][::-1])
            break #03

    aln1.reverse()
    aln2.reverse()

    score = M[-1][-1]

    return aln1, aln2, score


def is_atom(line):
    return line.startswith('ATOM') and line[13:15] == "CA" #04


def main(args):

    # Mobile
    with open(args[1]) as pdbfile:
        mobile = [ AA321.get(line[17:20],"x") for line in pdbfile if is_atom(line) ]#05

    # Mobile
    with open(args[2]) as pdbfile:
        fixed = [ AA321.get(line[17:20],"x") for line in pdbfile if is_atom(line) ]#06

    aligned1, aligned2, score= align(fixed, mobile)#11

    print("Alignment score:", score)

    colored1 = []
    colored2 = []
    for i in range(len(aligned1)):#07
        if aligned1[i] == aligned2[i]:
            aligned1[i] = RED + aligned1[i] + OFF #08
            aligned2[i] = RED + aligned2[i] + OFF

    print(OFF)
    for i in range(0, len(aligned1), 50):
        print("\n{:<10d}{:<10d}{:<10d}{:<10d}{:<10d}".format(i, i + 10, i + 20, i + 30, i + 40, i + 50)) #12
        print(5 * "0123456789")
        print(*(aligned1[i:i+50]), sep="", file=sys.stderr)
        print(*(aligned2[i:i+50]), sep="", file=sys.stderr)
    print('\033[0m')


sys.exit(main(sys.argv)) if __name__ == "__main__" else ... #09ß
