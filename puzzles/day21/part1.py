from utils.coordinates import YX
from utils.read_input import read_input
from utils.str_processing import filter_yx

map = [list(line) for line in read_input()]
start = next(filter_yx(map, lambda c: c == "S"))
steps = 64
visited = {0: {start}, 1: set[YX]()}
queues = {0: {start}, 1: set[YX]()}
for step in range(steps):
    q = queues[step % 2]
    next_q = set[YX]()
    next_v = visited[(step + 1) % 2]
    if not q:
        break
    for position in q:
        next_positions = {
            yx for yx in position.cross() if yx.is_in(map) and yx.on_wrapped(map) != "#"
        }
        next_q.update(next_positions.difference(next_v))
    next_v.update(next_q)
    queues[(step + 1) % 2] = next_q

print(len(visited[steps % 2]))
