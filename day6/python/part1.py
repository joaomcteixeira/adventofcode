import os
import sys
from math import floor, ceil
#from matplotlib import pyplot as plt
from pathlib import Path


def main(input_):

    lines = Path(input_).read_text().split(os.linesep)
    times = map(int, lines[0].split()[1:])
    records = map(int, lines[1].split()[1:])
    del lines

    result = 1
    for time, y in zip(times, records):

        # X where the parabola is max
        h = time / 2

        # max distance possible
        k = h * (time - h)

        a = -1 # by definition of the problem. Parabola facing down.

        # calculating X (pressing time) from Y

        #A = 1  # by definition: X^2, so we skip it
        B = -2 * h
        C = h**2 - ((y - k) / a)
        # x = (-B + (B**2-4*A*C)**0.5)/2*A
        x1 = (-B + (B**2 - 4 * C)**0.5) / 2
        x2 = (-B - (B**2 - 4 * C)**0.5) / 2

        wins = ceil(x1) - floor(x2) - 1
        result *= wins

        # Graphical representation
        #distances = [a*(x-h)**2+k for x in range(time + 1)]
        #plt.plot(distances, 'o-')
        #plt.axhline(y=y)
        #plt.axvline(x=x1, color='r')
        #plt.axvline(x=x2)
        #plt.axvline(x=h)
        #plt.show()

    return result


if __name__ == "__main__":
    print(main(sys.argv[1]))
