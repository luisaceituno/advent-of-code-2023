import re
from typing import Generator


def chars_surrounding(
    lines: list[str], y: int, x: int
) -> Generator[tuple[str, int, int], None, None]:
    moves = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for [mod_y, mod_x] in moves:
        cur_y = y + mod_y
        cur_x = x + mod_x
        if cur_x >= 0 and cur_y >= 0 and cur_y < len(lines):
            line = lines[cur_y]
            if cur_x < len(line):
                yield line[cur_x], cur_y, cur_x


def alphanum_tokens(line: str):
    return re.sub(r"[^0-9a-zA-Z]", " ", line).split()


def int_tokens(line: str):
    return [int(token) for token in re.sub(r"[^0-9\-]", " ", line).split()]
