import os
import re
import sys
from pathlib import Path
from math import prod


def main(input_):

    def look_for_number(lines, regex, ref_idx_range, maxidx, list_of_nums):
        """Look for a number close to the '*' (asterisk)."""
        for num in regex.finditer(lines):
            idx_range = set(range(num.start(), num.end()))
            if idx_range.intersection(ref_idx_range):
                list_of_nums.append(num.group())
            elif num.start() > maxidx:
                break
        return

    lines = Path(input_).read_text().split(os.linesep)

    if not lines[-1]:  # drop empty string at the end
        lines.pop()

    numre = re.compile(r'\d+')
    astre = re.compile(r'\*')

    # Solves IndexError for the first and last lines.
    # avoids using several 'ifs' inside the for loops
    lines = ['.' * len(lines[0])] + lines + ['.' * len(lines[0])]

    ratios = []
    numbers_per_ast = []
    max_end_index = len(lines[0]) - 1

    for i, line in enumerate(lines[1:-1], start=1):

        for asterisk in astre.finditer(line):

            # defines the range of indexes surrounding the asterisk
            _aststart = max(asterisk.start() - 1, 0)
            _astend = min(asterisk.end(), max_end_index) + 1
            idx_range = set(range(_aststart, _astend))

            for num in numre.finditer(lines[i]):

                if num.end() == asterisk.start():
                    numbers_per_ast.append(num.group())

                elif num.start() == asterisk.end():
                    numbers_per_ast.append(num.group())

                elif num.start() > asterisk.end():
                    break

            look_for_number(lines[i - 1], numre, idx_range, asterisk.end(), numbers_per_ast)
            look_for_number(lines[i + 1], numre, idx_range, asterisk.end(), numbers_per_ast)

            if len(numbers_per_ast) != 2:
                numbers_per_ast.clear()
            else:
                ratios.append(prod(map(int, numbers_per_ast)))
                numbers_per_ast.clear()

    return sum(ratios)


if __name__ == '__main__':
    print(main(sys.argv[1]))
