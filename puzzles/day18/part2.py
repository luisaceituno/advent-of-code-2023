import re
from puzzles.day18.common import blocky_shoelace
from utils.yx import DOWN, RIGHT, UP, LEFT, YX
from utils.read_input import read_input


lines = read_input()
corners: list[YX] = [YX(0, 0)]
pattern = re.compile(r"^(.) (\d+) \(#(\w+)\)$")
dirs = {"0": RIGHT, "2": LEFT, "3": UP, "1": DOWN}

for line in lines:
    _, _, color = pattern.search(line).groups()
    length = int(color[:-1], 16)
    dir = dirs[color[-1]]
    corners.append(corners[-1].move(dir, int(length)))


print(blocky_shoelace(corners))
