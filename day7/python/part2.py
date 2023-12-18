import os
import sys
from collections import Counter
from pathlib import Path

card_map = {c:i for i, c in enumerate('AKQT98765432J', start=1)}
type_map = {
    (5,): 1,
    (4, 1): 2,
    (3, 2): 3,
    (3, 1, 1): 4,
    (2, 2, 1): 5,
    (2, 1, 1, 1): 6,
    (1, 1, 1, 1, 1): 7,
    }


def sort(s):

    if 'J' in s and len(set(s)) > 1:  # avoids all Js
        min_value = 8
        card_types = set(s)
        card_types.remove('J')
        for card_type in card_types:
            new_J = s.replace('J', card_type)
            value = type_map[tuple(sorted(Counter(new_J).values(), reverse=True))]
            min_value = min(min_value, value)
    else:
        min_value = type_map[tuple(sorted(Counter(s).values(), reverse=True))]

    b = tuple(card_map[c] for c in s)
    return (min_value,) + b


def main(input_):
    lines = Path(input_).read_text().split(os.linesep)
    lines.sort(key=lambda x: sort(x[:5]), reverse=True)
    total = 0
    for i, line in enumerate(lines, start=1):
        hand, bid = line.split()
        total += i * int(bid)

    return total


if __name__ == '__main__':
    print(main(sys.argv[1]))
