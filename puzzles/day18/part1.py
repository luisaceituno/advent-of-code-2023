import re
from puzzles.day18.common import blocky_shoelace
from utils.coordinates import DOWN, RIGHT, UP, LEFT, YX
from utils.read_input import read_input


lines = read_input()
corners: list[YX] = [YX(0, 0)]
pattern = re.compile(r"^(.) (\d+) \(#(\w+)\)$")
dirs = {"R": RIGHT, "L": LEFT, "U": UP, "D": DOWN}

for line in lines:
    dir_key, length, color = pattern.search(line).groups()
    dir = dirs[dir_key]
    corners.append(corners[-1].move(dir, int(length)))

print(blocky_shoelace(corners))
