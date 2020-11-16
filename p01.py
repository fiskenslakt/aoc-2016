from collections import deque

from aocd import data


directions = data.split(', ')

movement_map = {'N': 1, 'E': 1j,
                'S': -1,'W': -1j}

visited_twice_pos = None
seen = set([0j])
position = 0j
facing = deque(['N','E','S','W'])

for direction in directions:
    d = direction[0]
    s = int(direction[1:])

    if d == 'R':
        facing.rotate(1)
    elif d == 'L':
        facing.rotate(-1)

    for _ in range(s):
        position += movement_map[facing[0]]

        if visited_twice_pos is not None:
            continue

        if position not in seen:
            seen.add(position)
        else:
            visited_twice_pos = position

end_dist = int(abs(position.real) + abs(position.imag))
print('Part 1:', end_dist)

visited_twice_dist = int(abs(visited_twice_pos.real) + abs(visited_twice_pos.imag))
print('Part 2:', visited_twice_dist)
