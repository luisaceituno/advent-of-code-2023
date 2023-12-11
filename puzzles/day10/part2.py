from puzzles.day10.common import next_pos
from utils.coordinates import YX
from utils.read_input import read_input
from utils.str_processing import find_y_x_val

input = [list(line) for line in read_input()]

y, x, s = find_y_x_val(input, lambda s: s == "S")
start = YX(y, x)
move = (
    start,
    next(yx for yx in start.cross() if yx.is_in(input) and next_pos(start, yx, input)),
)

loop = {start}
while move[1] != start:
    loop.add(move[1])
    move = (move[1], next_pos(move[0], move[1], input))

if start.up() in loop:
    if start.right() in loop:
        input[start.y][start.x] = "L"
    if start.down() in loop:
        input[start.y][start.x] = "|"
    if start.left() in loop:
        input[start.y][start.x] = "J"
elif start.down() in loop:
    if start.right() in loop:
        input[start.y][start.x] = "F"
    if start.left() in loop:
        input[start.y][start.x] = "7"
else:
    input[start.y][start.x] = "-"

counter = 0
for y in range(0, len(input)):
    outside = True
    buffer = 0
    for x in range(0, len(input[y])):
        cur = YX(y, x)
        if cur in loop:
            type = input[cur.y][cur.x]
            if type in "F7":
                if buffer > 0:
                    buffer = 0
                    outside = not outside
                else:
                    buffer = (buffer - 1) % -2
            elif type in "LJ":
                if buffer < 0:
                    buffer = 0
                    outside = not outside
                else:
                    buffer = (buffer + 1) % 2
            elif type == "|":
                outside = not outside
        elif not outside:
            counter += 1

print(counter)
