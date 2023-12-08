from utils.read_input import read_input
from utils.str_processing import alphanum_tokens

lines = read_input()
instructions = lines[0]

paths: dict[str, tuple[str, str]] = {}
for line in lines[2:]:
    source, target_l, target_r = alphanum_tokens(line)
    paths[source] = (target_l, target_r)


def repeat_forever(texts: list[str]):
    while True:
        for text in texts:
            yield text


cur = "AAA"
path_len = 0
for move in repeat_forever(instructions):
    cur = paths[cur][0 if move == "L" else 1]
    path_len += 1
    if cur == "ZZZ":
        break
print(path_len)
