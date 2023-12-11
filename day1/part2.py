import sys
import re

regex = re.compile(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))')

numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    }

def yield_digits(input_):
    with open(input_, 'r') as fin:
        for line in fin:
            digits = regex.findall(line.strip())
            first = numbers.get(digits[0], digits[0])
            second = numbers.get(digits[-1], digits[-1])
            yield int(first + second)

total = sum(yield_digits(sys.argv[1]))
print(total)

