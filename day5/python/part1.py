import sys
import os
from pathlib import Path


def main(input_):

    def lookup(maps, code, map_idx):
        try:
            for dest, src, rng in maps[map_idx]:
                if code in range(src, src + rng):
                    new_dest = code - src + dest
                    return lookup(maps, new_dest, map_idx + 1)
            else:
                return lookup(maps, code, map_idx + 1)
        except IndexError:
            return code

    lines = Path(input_).read_text().split(os.linesep)

    seeds = list(map(int, lines[0].split(':')[1].split()))

    # create maps for dest, source, range
    # the maps are always in order, meaning one map always maps to the
    # next map.
    maps = []
    for line in lines[1:]:
        if not line:
            continue
        if line[0].isalpha():
            maps.append([])
        elif line[0].isdigit():
            maps[-1].append(tuple(map(int, line.split())))

    #locations = []
    #for seed in seeds:
    #    locations.append(lookup(maps, seed, 0))

    return min(lookup(maps, seed, 0) for seed in seeds)

if __name__ == '__main__':
    print(main(sys.argv[1]))
