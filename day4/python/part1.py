import sys


def main(input_):

    def parse_line(line):
        blocks = line.split(':')[1].split('|')
        valid = set(map(int, blocks[0].strip().split()))
        mine = set(map(int, blocks[1].strip().split()))
        return valid, mine

    result = 0

    with open(input_, 'r') as fin:

        for line in fin:

            valid_nums, my_nums = parse_line(line)

            winning = my_nums.intersection(valid_nums)

            if winning:
                result += 1 if len(winning) == 1 else 2**(len(winning) - 1)

    return result


if __name__ == '__main__':
    print(main(sys.argv[1]))
