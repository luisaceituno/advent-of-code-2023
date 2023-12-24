from queue import Queue
from typing import NamedTuple
from utils.read_input import read_input
from utils.str_processing import int_tokens
from utils.yx import YX
from utils.zyx import ZYX


class Brick(NamedTuple):
    p1: ZYX
    p2: ZYX

    def blocks(s):
        start, end = sorted((s.p1, s.p2))
        yield start
        dz, dy, dx = start.direction_to(end)
        while start != end:
            start = ZYX(start.z + dz, start.y + dy, start.x + dx)
            yield start

    def altitude_start(self):
        return self.p1.z

    def height(self):
        return 1 + self.p2.z - self.p1.z


bricks = {
    Brick(*sorted([ZYX(z1, y1, x1), ZYX(z2, y2, x2)]))
    for x1, y1, z1, x2, y2, z2 in [int_tokens(line) for line in read_input()]
}

floors: dict[YX, Brick] = {}
heights: dict[Brick, int] = {}
beneath: dict[Brick, set[Brick]] = {}
above: dict[Brick, set[Brick]] = {}
for brick in sorted(bricks, key=lambda b: b.altitude_start()):
    candidates = set[Brick]()
    heights[brick] = 0 + brick.height()
    for z, y, x in brick.blocks():
        pos = YX(y, x)
        if pos in floors:
            if floors[pos] == brick:
                break
            candidates.add(floors[pos])
        floors[pos] = brick
    if candidates:
        max_z = max(heights[c] + c.height() for c in candidates)
        supports = {c for c in candidates if heights[c] + c.height() == max_z}
        beneath.setdefault(brick, set()).update(supports)
        for support in supports:
            above.setdefault(support, set()).add(brick)
        heights[brick] = max_z + brick.height()


def part1():
    count = 0
    for brick in bricks:
        if brick not in above:
            count += 1
        else:
            count += (
                1
                if all(len(beneath[brick_above]) > 1 for brick_above in above[brick])
                else 0
            )
    print("Part 1:", count)


def part2():
    sum = 0
    for brick in bricks:
        chain = set[Brick]()
        queue = Queue[Brick]()
        queue.put(brick)
        while not queue.empty():
            cur = queue.get()
            if cur in chain:
                continue
            chain.add(cur)
            for a in above.setdefault(cur, set()):
                if all((b in chain) for b in beneath[a]):
                    if a not in chain:
                        queue.put(a)
        sum += len(chain) - 1

    print("Part 2:", sum)


part1()
part2()
