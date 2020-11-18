from aocd import data


possible = 0
rows = []

for triangle in data.splitlines():
    sides = [int(side) for side in triangle.split()]
    rows.append(sides)
    sides = sorted(sides)
    if sum(sides[:2]) > sides[-1]:
        possible += 1

print('Part 1:', possible)

possible = 0
vert_triangles = [side for column in zip(*rows) for side in column]

for triangle in zip(*[iter(vert_triangles)]*3):
    sides = sorted(triangle)
    if sum(sides[:2]) > sides[-1]:
        possible += 1

print('Part 2:', possible)
