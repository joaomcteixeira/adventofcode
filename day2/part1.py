import sys
import re


def main(input_):

    d_max = {
        'red':12,
        'green':13,
        'blue':14,
        }

    total = 0

    regex = re.compile(r'\d+|red|blue|green')

    with open(input_, 'r') as fin:

        for line in fin:

            items = regex.findall(line)
            current_id = items[0]
            counts = items[1::2]
            colors = items[2::2]

            for color, count in zip(colors, counts):
                if int(count) > d_max[color]:
                    break
            else:
                total += int(current_id)

    print(total)
    return


if __name__ == '__main__':
    main(sys.argv[1])
