#!/env python3
"""
This module counts the genera, the number of species per genus and the number of species per countries
usage: fixme.py Birds.txt
"""

__author__ = 'Fenna Feenstra'
__version__ = '0.3'

# imports
import sys

# globals
genera = dict()
countrylist = dict()


def count_birds(filename):
    with open(filename, 'r') as f:
        for line in filename:
            if not line.strip().startswith("SOORT"):
                storeline(line)

# functions
def storeline(data):
    p = "([A-Z][a-z]+) ([a-z]+);(.+)"
    m = re.search(p, data)
    if m:
        genus = m.group(1)
        if not genus in genera:genera[genus]=0
        genera[genus] +=1

        countries = m.group(3).split('')
        for c in countries:
            if c in countrylist: countrylist[c]=0
            countrylist[c]+=1

def print_results()
    print("\ngenus aantal: {}".format(len(genera)))
    print('-'*40)
    for g, n in genera.items():
        print("aantal vogelsoorten per genus {}: ".format(g, n))
    print('-'*40)
    for c, n in countrylist.items():
        print("aantal vogelsoorten per land {}: {}".format(c, n))


def main(argv=None):
    argv = sys.argv
    for filename in argv[1:]:
        count_birds(filename)
        print_results()
    return 0


if __name__ == '__main__':
    sys.exit()
