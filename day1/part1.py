import sys
import re

regex = re.compile(r'\d')

def yield_digits(input_):
    with open(input_, 'r') as fin:
        for line in fin:
            digits = regex.findall(line.strip())
            yield int(digits[0] + digits[-1])

total = sum(yield_digits(sys.argv[1]))
print(total)

