import sys
import pprint


def main(input_):

    def parse_line(line):
        blocks = line.split(':')[1].split('|')
        valid = set(map(int, blocks[0].strip().split()))
        mine = set(map(int, blocks[1].strip().split()))
        return valid, mine

    result = 0

    matching_numbers = {}

    with open(input_, 'r') as fin:

        for i, line in enumerate(fin, start=1):

            valid_nums, my_nums = parse_line(line)
            match_numbers = my_nums.intersection(valid_nums)
            matching_numbers[i] = len(match_numbers)

    copies = {i:1 for i in matching_numbers.keys()}

    for card, matching in matching_numbers.items():
        for _ in range(copies[card]):
            for i in range(card + 1, card + matching + 1):
                copies[i] += 1

    return sum(v for v in copies.values())


if __name__ == '__main__':
    print(main(sys.argv[1]))
