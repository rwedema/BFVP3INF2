#!/usr/bin/env python3

"""
Draw a sierpinski triangle using turtle graphics
"""

__author__ = "Tsjerk A. Wassenaar"


import sys
import turtle


def actions(step=5, angle=90):
    """Return dictionary with control functions for L-system"""

    def forward(turt):
        turt.forward(step)

    def right(turt):
        turt.right(angle)

    def left(turt):
        turt.left(angle)

    return {'F': forward, 'f': forward, '+': right, '-': left}


def l_system(depth, axiom, **rules):
    """Generate L-system from axiom using rules, up to given depth"""

    if not depth:
        return axiom
    
    # Basic, most straight-forward implementation
    # Note 1: it doesn't matter if axiom is a string or a list
    # Note 2: consider the difference between .extend() and .append()
    out = []
    for char in axiom:
        if char in rules:
            out.extend(rules[char])
        else:
            out.append(char)
    
    # Two alternative implementations. If you want to try 
    # an alternative, comment out the original first.
    # It won't change the answer, but it will take more time
    # if you keep the code active.
    
    # I. Alternative implementation using dict.get
    # --------------------------------------------
    # out = []
    # for char in axiom:
    #     out.extend(rules.get(char, [char]))
    
    # II. Alternative implementation in one line using list comprehension
    # -------------------------------------------------------------------
    # out = [i for char in axiom for i in rules.get(char, char)]
    
    # Note 3: See how comments are used to annotate the code... :)
    
    return l_system(depth - 1, out, **rules)


def sierpinski(depth):
    return l_system(depth, 'F-f-f', F='F-f+F+f-F', f='ff')


def main(args):
    """Main function"""
    
    # Preparation
    don = turtle.Turtle(shape="turtle")
    don.speed(0)
    actdict = actions(step=5, angle=120)

    # Work
    for char in sierpinski(6):
        if char in actdict:
            actdict[char](don)

    # Finish
    input('Press any key to continue')

    return 0


if __name__ == "__main__":
    excode = main(sys.argv)
    sys.exit(excode)


