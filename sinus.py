#!/usr/bin/env python3

"""
program that plots a sinus wave
    usage: sinus.py
"""

__author__ = "F.Feenstra"

## CODE
import matplotlib.pyplot as plt
import numpy as np
import sys

sample_rate = 140
frequency = 4
amplitude = 2
phase = 0.5


def comp_y(t):
    """compute the y value of the sin wave at the for a specific sample"""
    y_t = amplitude * np.sin(2*np.pi * frequency * (t/sample_rate) + phase)
    return y_t

def comp_amplitude(x):
    """compute the y value of the sin wave at the for each sample"""
    y = []
    for t in x:
        y.append(comp_y(t))
    return y

def main(args):
    x = np.arange(sample_rate) # the points on the x axis for plotting
    y = comp_amplitude(x) # the points on the y axis for plotting
    plt.plot(x,y)
    plt.show()
    return 0


if __name__ == "__main__":
    exitcode = main(sys.argv)
    sys.exit(exitcode)
