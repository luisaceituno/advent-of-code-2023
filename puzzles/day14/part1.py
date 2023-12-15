from itertools import chain
from utils.lists import enumerate_2d, filter_2d
from utils.read_input import read_input


lines: list[list[str]] = read_input()
cubes: set[tuple[int, int]] = set()
spheres: set[tuple[int, int]] = set()

for e, y, x in enumerate_2d(lines):
    if e == "#":
        cubes.add((y, x))
    elif e == "O":
        spheres.add((y, x))

load = 0
for y, x in sorted(spheres, key=lambda s: s[0]):
    yy = y
    while yy > 0:
        if (yy - 1, x) not in cubes and (yy - 1, x) not in spheres:
            yy = yy - 1
        else:
            break
    spheres.remove((y, x))
    spheres.add((yy, x))
    load += len(lines) - yy

print(load)
