from puzzles.day10.common import next_pos
from utils.yx import YX
from utils.lists import filter_2d
from utils.read_input import read_input

input = read_input()

s, y, x = next(filter_2d(input, lambda s: s == "S"))
start = YX(y, x)
path1, path2 = [
    (start, cur)
    for cur in YX(y, x).cross()
    if cur.is_in(input) and next_pos(start, cur, input)
]

steps = 1
while path1[1] != path2[1]:
    path1 = [path1[1], next_pos(path1[0], path1[1], input)]
    path2 = [path2[1], next_pos(path2[0], path2[1], input)]
    steps += 1

print(steps)
