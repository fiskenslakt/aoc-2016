import re

from string import ascii_lowercase as alpha
from collections import Counter

from aocd import data


def decrypt_room(room):
    rotation = int(room.group('sector')) % 26
    table = str.maketrans(alpha, alpha[rotation:] + alpha[:rotation])

    return str.translate(room.group('name'), table)


room_pattern = re.compile(r'(?P<name>.+)-(?P<sector>\d+)\[(?P<checksum>\w+)]')

sector_sum = 0
storage_location = None

for room in data.splitlines():
    room = room_pattern.search(room)
    decrypted_name = decrypt_room(room)

    if storage_location is None and 'northpole' in decrypted_name:
        storage_location = room

    name = room.group('name').replace('-', '')
    most_common = sorted(Counter(name).most_common(), key=lambda t: (-t[1],t[0]))[:5]
    checksum = ''.join((t[0] for t in most_common))

    if checksum == room.group('checksum'):
        sector_sum += int(room.group('sector'))

print('Part 1:', sector_sum)
print('Part 2:', storage_location.group('sector'))
