import hashlib

from aocd import data as door_id


password1 = ''
password2 = [None]*8
password2_found = False
index = 0
indicies = set()

while not password2_found:
    door_hash = hashlib.md5(f'{door_id}{index}'.encode()).hexdigest()

    if door_hash[:5] == '0'*5:
        if len(password1) != 8:
            password1 += door_hash[5]

        if '0' <= door_hash[5] <= '7' and int(door_hash[5]) not in indicies:
            password2[int(door_hash[5])] = door_hash[6]
            indicies.add(int(door_hash[5]))

        if len(indicies) == 8:
            password2_found = True

    index += 1

print('Part 1:', password1)
print('Part 2:', ''.join(password2))
