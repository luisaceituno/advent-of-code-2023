from functools import reduce
import numpy
from utils.read_input import read_input
from utils.str_processing import alphanum_tokens


def repeat_forever(texts: list[str]):
    while True:
        for text in texts:
            yield text


def path_lengths(start: str, limit: int = 1):
    cur = start
    path_len = 0
    path_lens: list[int] = []
    for move in repeat_forever(instructions):
        cur = paths[cur][0 if move == "L" else 1]
        path_len += 1
        if cur[-1] == "Z":
            path_lens.append(path_len)
            if len(path_lens) >= limit:
                break
    return path_lens


lines = read_input()
instructions = lines[0]

paths: dict[str, tuple[str, str]] = {}
for line in lines[2:]:
    source, target_l, target_r = alphanum_tokens(line)
    paths[source] = (target_l, target_r)

starts = [key for key in paths.keys() if key[-1] == "A"]
possible_lengths = [path_lengths(start, limit=1) for start in starts]

result = reduce(numpy.lcm, possible_lengths)
print(min(result))
