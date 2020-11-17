from aocd import data

possible = 0

for triangle in data.split('\n'):
    sides = sorted(int(side) for side in triangle.split())
    if sum(sides[:2]) > sides[-1]:
        possible += 1

print(possible)
