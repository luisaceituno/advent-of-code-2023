from utils.yx import DOWN, LEFT, RIGHT, UP, YX


def next_pos(prev: YX, cur: YX, input: list[str]):
    type = input[cur.y][cur.x]
    if type == "F":
        if prev == cur.move(DOWN):
            return cur.move(RIGHT)
        if prev == cur.move(RIGHT):
            return cur.move(DOWN)
    if type == "-":
        if prev == cur.move(LEFT):
            return cur.move(RIGHT)
        if prev == cur.move(RIGHT):
            return cur.move(LEFT)
    if type == "7":
        if prev == cur.move(LEFT):
            return cur.move(DOWN)
        if prev == cur.move(DOWN):
            return cur.move(LEFT)
    if type == "|":
        if prev == cur.move(UP):
            return cur.move(DOWN)
        if prev == cur.move(DOWN):
            return cur.move(UP)
    if type == "L":
        if prev == cur.move(UP):
            return cur.move(RIGHT)
        if prev == cur.move(RIGHT):
            return cur.move(UP)
    if type == "J":
        if prev == cur.move(LEFT):
            return cur.move(UP)
        if prev == cur.move(UP):
            return cur.move(LEFT)
