import os
import sys
from math import floor, ceil
#from matplotlib import pyplot as plt
from pathlib import Path


def main(input_):

    lines = Path(input_).read_text().split(os.linesep)
    time = int(''.join(lines[0].split()[1:]))
    record = int(''.join(lines[1].split()[1:]))
    del lines

    # X where the parabola is max
    h = time / 2

    # max distance possible
    k = h * (time - h)

    a = -1 # by definition of the problem. Parabola facing down.

    # calculating X (pressing time) from Y
    #A = 1  # by definition: X^2, so we skip it
    B = -2 * h
    C = h**2 - ((record - k) / a)
    # x = (-B + (B**2-4*A*C)**0.5)/2*A
    x1 = (-B + (B**2 - 4 * C)**0.5) / 2
    x2 = (-B - (B**2 - 4 * C)**0.5) / 2

    result = ceil(x1) - floor(x2) - 1
    return result


if __name__ == "__main__":
    print(main(sys.argv[1]))
