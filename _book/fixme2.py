#!/usr/env python3

"""
Draw a tree using turtle
"""

__author__ = "Fenna Feenstra"

import sys

def tree(branchLen): 
    """ function that draws the tree with stem and branches upwards"""
    if branchLen > 5:
        t.backward(branchLen)
        t.right(20)
        tree(branchLen-16,t)
        t.left(40)
        tree(branchLen-16,t)
        t.right(20)
        t.forward(branchLen)


def init_turtle()
    """ function that initializes and returns the turtle"""
    t = turtle.Turtle()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("darkgreen")



def main(args=None):
    """ main function """
    myWin= turtle.Screen
    t = init_turtle()
    if len(args) < 2:
        tree(80, t)
    else:
        tree(args[2], t)
    myWin.exitonclick()


if "__name__" == "__main__":
    excode = main(sys.argv)
    sys.exit(excode)
