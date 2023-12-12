import re
import sys
from math import prod


def main(input_):

    regex = re.compile(r'\d+|red|blue|green')
    d = {'red': [], 'green': [], 'blue': []}
    total = 0

    with open(input_, 'r') as fin:

        for line in fin:

            [v.clear() for v in d.values()]

            items = regex.findall(line)
            counts = items[1::2]
            colors = items[2::2]

            for color, count in zip(colors, counts):
                d[color].append(int(count))

            total += prod(max(v) for v in d.values())

    return total


if __name__ == '__main__':
    print(main(sys.argv[1]))
