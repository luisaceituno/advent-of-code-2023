from itertools import chain
import time
import timeit
from utils.lists import cycle_n, enumerate_2d
from utils.read_input import read_input

lines: list[list[str]] = read_input()
cubes: set[tuple[int, int]] = set()
spheres: set[tuple[int, int]] = set()

for e, y, x in enumerate_2d(lines):
    if e == "#":
        cubes.add((y, x))
    elif e == "O":
        spheres.add((y, x))

sorts = {
    "n": lambda yx: yx[0],
    "w": lambda yx: yx[1],
    "s": lambda yx: -yx[0],
    "e": lambda yx: -yx[1],
}

moves = {
    "n": lambda y, x: (y - 1, x),
    "w": lambda y, x: (y, x - 1),
    "s": lambda y, x: (y + 1, x),
    "e": lambda y, x: (y, x + 1),
}

dirs = ["n", "w", "s", "e"]
cycles = 1000000000
cache = {}
max_y = len(lines)
max_x = len(lines[0])
loads = {}

cycle = 0
while cycle < cycles:
    for dir in dirs:
        for y, x in sorted(spheres, key=sorts[dir]):
            targety, targetx = y, x
            while True:
                yy, xx = moves[dir](targety, targetx)
                if (
                    0 <= yy < max_y
                    and 0 <= xx < max_x
                    and (yy, xx) not in spheres
                    and (yy, xx) not in cubes
                ):
                    targety, targetx = yy, xx
                else:
                    break
            spheres.remove((y, x))
            spheres.add((targety, targetx))
    s_hash = frozenset(spheres)
    if s_hash in cache:
        prev = cache.get(s_hash)
        length = cycle - prev
        rest = (cycles - cycle) % length
        print(loads[prev - 1 + rest])
        break
    cache[s_hash] = cycle
    loads[cycle] = sum(len(lines) - y for y, x in spheres)
    cycle += 1
