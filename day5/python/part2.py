import sys
import os
from pathlib import Path
from matplotlib import pyplot as plt
from math import inf
from operator import add, sub


def lookup(maps, code, map_idx):
    # recursive approach to map from seed to location
    try:
        for dest, src, rng in maps[map_idx]:
            if code in range(src, src + rng):
                new_dest = code - src + dest
                return lookup(maps, new_dest, map_idx + 1)
        else:
            return lookup(maps, code, map_idx + 1)
    except IndexError:
        return code


def fine_search(minval, ss, sr, major_step, maps, func):
    jump = sr // major_step
    prev_min = minval
    prev_ss = ss
    while True:
        ss = func(ss, jump)
        minval = lookup(maps, ss, 0)
        if minval < prev_min:
            prev_ss = ss
            prev_min = minval

        elif minval > prev_min and jump == 1:
            minval = prev_min
            break

        else:
            ss = prev_ss
            jump = max(jump // 10, 1)

    return minval


def main(input_):

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

    seed_starts = seeds[0::2]
    seed_rng = seeds[1::2]
    prev_min_val = inf
    major_step = 1000
    for ss, sr in zip(seed_starts, seed_rng):

        # we need to create a list because we need to retrive the seed
        # representing the local minimum
        seeds_ = list(range(ss, ss+sr, max(sr // major_step, 1)))

        # do a coarse-grain search for the local minimum
        minvals = [lookup(maps, seed, 0) for seed in seeds_]

        # finds the seed of the local minimum
        minval = min(minvals)
        idx = minvals.index(minval)
        ss = seeds_[idx]

        if lookup(maps, ss + 1, 0) < minval:  # minimum is at the right
            # therefore, we search by increasing the seed number
            minval = fine_search(minval, ss, sr, major_step, maps, add)

        if lookup(maps, ss - 1, 0) < minval:  # minimum is at the left
            # therefore, we search by decreasing the seed number
            minval = fine_search(minval, ss, sr, major_step, maps, sub)

        # keep the minimum location value over the seed ranges
        prev_min_val = min(minval, prev_min_val)

    return prev_min_val


if __name__ == '__main__':
    print(main(sys.argv[1]))
