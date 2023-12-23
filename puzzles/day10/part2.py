from puzzles.day10.common import next_pos
from utils.yx import DOWN, LEFT, RIGHT, UP, YX
from utils.lists import filter_2d
from utils.read_input import read_input

input = [list(line) for line in read_input()]

s, y, x = next(filter_2d(input, lambda s: s == "S"))
start = YX(y, x)
move = (
    start,
    next(yx for yx in start.cross() if yx.is_in(input) and next_pos(start, yx, input)),
)

loop = {start}
while move[1] != start:
    loop.add(move[1])
    move = (move[1], next_pos(move[0], move[1], input))

if start.move(UP) in loop:
    if start.move(RIGHT) in loop:
        input[start.y][start.x] = "L"
    if start.move(DOWN) in loop:
        input[start.y][start.x] = "|"
    if start.move(LEFT) in loop:
        input[start.y][start.x] = "J"
elif start.move(DOWN) in loop:
    if start.move(RIGHT) in loop:
        input[start.y][start.x] = "F"
    if start.move(LEFT) in loop:
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
