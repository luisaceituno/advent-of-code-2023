from utils.yx import YX
from utils.read_input import read_input
from utils.str_processing import filter_yx

map = [list(line) for line in read_input()]
start = next(filter_yx(map, lambda c: c == "S"))

cycle = len(map)
half = len(map) // 2
steps = half + cycle * 2  # 26501365 = 65 + 202300 * 131 and the input is 131 * 131
visited = {0: {start}, 1: set[YX]()}
queues = {0: {start}, 1: set[YX]()}
marks: list[int] = []
for step in range(steps):
    q = queues[step % 2]
    next_q = set[YX]()
    next_v = visited[(step + 1) % 2]
    for position in q:
        next_positions = {yx for yx in position.cross() if yx.on_wrapped(map) != "#"}
        next_q.update(next_positions.difference(next_v))
    next_v.update(next_q)
    queues[(step + 1) % 2] = next_q
    if (step + 1 - half) % cycle == 0:
        marks.append(len(next_v))

d1 = marks[1] - marks[0]
d2 = marks[2] - marks[1]
dd = d2 - d1
magic = marks[2] - marks[1] - 2 * dd
cycles = (26501365 - half) / cycle
result = marks[0] + magic * cycles + dd * (cycles * (cycles + 1) / 2)
print(int(result))
