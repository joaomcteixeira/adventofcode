import os
import re
import sys
from pathlib import Path


def main(input_):

    def is_symbol(chars):
        return not all(char in '1234567890.' for char in chars)

    lines = Path(input_).read_text().split(os.linesep)

    if not lines[-1]:  # drop empty string
        lines.pop()

    regex = re.compile(r'\d+')

    # Solves IndexError for the first and last lines.
    lines = ['.' * len(lines[0])] + lines + ['.' * len(lines[0])]

    valid_numbers = []
    max_end_index = len(lines[0]) - 1

    for i, line in enumerate(lines[1:-1], start=1):
        for found in regex.finditer(line):

            start = found.start()
            end = found.end()

            if \
                    (is_symbol(lines[i][max(start - 1, 0)]) or is_symbol(lines[i][min(end, max_end_index)])) \
                    or is_symbol(lines[i - 1][max(start - 1, 0):end + 1]) \
                    or is_symbol(lines[i + 1][max(start - 1, 0):end + 1]):

                valid_numbers.append(int(found.group()))

    return sum(valid_numbers)


if __name__ == '__main__':
    print(main(sys.argv[1]))
