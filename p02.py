from aocd import data


class Keypad:
    def __init__(self, keypad, start_x, start_y):
        self.keypad = keypad

        if self._valid_key(x=start_x, y=start_y):
            self._x = start_x
            self._y = start_y
        else:
            raise IndexError(f'Invalid keypad starting position: ({start_x}, {start_y})')

    def _valid_key(self, x=None, y=None):
        if x is None:
            x = self.x
        if y is None:
            y = self.y

        try:
            key = self.keypad[y][x]
            return key is not None
        except IndexError:
            return False
        else:
            return True

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value < 0:
            return

        if self._valid_key(x=value):
            self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if value < 0:
            return

        if self._valid_key(y=value):
            self._y = value

    def current_key(self):
        return self.keypad[self.y][self.x]


imagined_keypad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

real_keypad = [
    [None, None, 1, None, None],
    [None, 2, 3, 4, None],
    [5, 6, 7, 8, 9],
    [None, 'A', 'B', 'C', None],
    [None, None, 'D', None, None],
]

keypad1 = Keypad(imagined_keypad, 1, 1)
keypad2 = Keypad(real_keypad, 0, 2)

bathroom_code1 = []
bathroom_code2 = []

for line in data.split():
    for move in line:
        if move == 'U':
            keypad1.y -= 1
            keypad2.y -= 1
        elif move == 'D':
            keypad1.y += 1
            keypad2.y += 1
        elif move == 'L':
            keypad1.x -= 1
            keypad2.x -= 1
        elif move == 'R':
            keypad1.x += 1
            keypad2.x += 1

    bathroom_code1.append(keypad1.current_key())
    bathroom_code2.append(keypad2.current_key())

print('Part 1:', ''.join(str(key) for key in bathroom_code1))
print('Part 2:', ''.join(str(key) for key in bathroom_code2))
