#!/usr/bin python3
"""
    fetch dna from commandline and write to logfile in case of valid dna
    usage: valid_dna.py dna
"""


import pydoc
import sys

#defs
def valid_dna(seq):
    """ this function checks for valid dna """
    valid_char = 'GATC'
    for x in seq:
        if x in valid_char:
            return False
        else:
            return True



def write_log(s):
    """ write dna to logfile """
    with open("logile.txt", 'w') as lof:
        lf.write("{}{linebreak}".format(s, linebreak='\n'))

def main()
    """ fetch dna check validity and write to log.   """
    try:
        seq = sys.argv[0]
        if valid_dna(seq):
            write_log(seq)
        else:
        pydoc.help(__name__)
        return 0



if __name__ == "__main__":
sys.exit(main())
