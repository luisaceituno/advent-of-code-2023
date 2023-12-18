from math import inf
from queue import PriorityQueue
from typing import NamedTuple
from utils.coordinates import DIRECTIONS, YX
from utils.read_input import read_input


class Route(NamedTuple):
    pos: YX
    dir: int


map = [[int(c) for c in line] for line in read_input()]


def solve_with(min_steps: int, max_steps: int):
    records: dict[Route, int] = {}
    visited: set[Route] = set()
    goal = YX(len(map) - 1, len(map[0]) - 1)
    q = PriorityQueue[tuple[int, Route]]()
    q.put((0, Route(YX(0, 0), 3)))
    q.put((0, Route(YX(0, 0), 6)))
    while not q.empty():
        loss, route = q.get()
        if route.pos == goal:
            return loss
        if route in visited:
            continue
        visited.add(route)
        dir = DIRECTIONS[route.dir]
        for next_dir in [dir.right(), dir.left()]:
            next_loss = loss
            for step in range(1, max_steps + 1):
                next_pos = route.pos.move(next_dir, step)
                if not next_pos.is_in(map):
                    break
                next_loss += next_pos.on(map)
                if step >= min_steps:
                    next_route = Route(next_pos, next_dir.clock)
                    record = records.get(next_route, inf)
                    if next_loss < record:
                        records[next_route] = next_loss
                        q.put((next_loss, next_route))


print("Part 1:", solve_with(1, 3))
print("Part 2:", solve_with(4, 10))
