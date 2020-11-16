from aocd import data


keypad = {
    1: {'R': 2, 'D': 4},
    2: {'L': 1, 'R': 3, 'D': 5},
    3: {'L': 2, 'D': 6},
    4: {'U': 1, 'R': 5, 'D': 7},
    5: {'U': 2, 'L': 4, 'R': 6, 'D': 8},
    6: {'U': 3, 'L': 5, 'D': 9},
    7: {'U': 4, 'R': 8},
    8: {'L': 7, 'U': 5, 'R': 9},
    9: {'L': 8, 'U': 6},
}

current_key = 5
bathroom_code = []

for line in data.split():
    for move in line:
        current_key = keypad[current_key].get(move, current_key)

    bathroom_code.append(current_key)

print('Part 1:', ''.join(str(key) for key in bathroom_code))
