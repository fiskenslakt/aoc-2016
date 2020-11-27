from collections import Counter

from aocd import data


message = ''
real_message = ''

for column in zip(*data.splitlines()):
    frequencies = Counter(column).most_common()
    message += frequencies[0][0]
    real_message += frequencies[-1][0]

print('Part 1:', message)
print('Part 2:', real_message)
