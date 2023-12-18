from math import inf
from queue import PriorityQueue
from typing import Callable, NamedTuple
from utils.coordinates import YX
from utils.read_input import read_input


class Route(NamedTuple):
    pos: YX
    dir: int


class Dir(NamedTuple):
    possible_turns: list[int]
    move: Callable[[YX, int], YX]


dirs = {
    0: Dir([3, 6], None),
    12: Dir([3, 9], YX.up),
    3: Dir([6, 12], YX.right),
    6: Dir([3, 9], YX.down),
    9: Dir([6, 12], YX.left),
}
map = [[int(c) for c in line] for line in read_input()]


def solve_with(min_steps: int, max_steps: int):
    records: dict[Route, int] = {}
    visited: set[Route] = set()
    goal = YX(len(map) - 1, len(map[0]) - 1)
    q = PriorityQueue[tuple[int, Route]]()
    q.put((0, Route(YX(0, 0), 0)))
    while not q.empty():
        loss, route = q.get()
        if route.pos == goal:
            return loss
        if route in visited:
            continue
        visited.add(route)
        dir = dirs[route.dir]
        for next_dir_key in dir.possible_turns:
            next_dir = dirs[next_dir_key]
            next_loss = loss
            for step in range(1, max_steps + 1):
                next_pos = next_dir.move(route.pos, step)
                if not next_pos.is_in(map):
                    break
                next_loss += next_pos.on(map)
                if step >= min_steps:
                    next_route = Route(next_pos, next_dir_key)
                    record = records.get(next_route, inf)
                    if next_loss < record:
                        records[next_route] = next_loss
                        q.put((next_loss, next_route))


print("Part 1:", solve_with(1, 3))
print("Part 2:", solve_with(4, 10))
