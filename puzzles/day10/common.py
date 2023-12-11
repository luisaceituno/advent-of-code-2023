from utils.coordinates import YX


def next_pos(prev: YX, cur: YX, input: list[str]):
    type = input[cur.y][cur.x]
    if type == "F":
        if prev == cur.down():
            return cur.right()
        if prev == cur.right():
            return cur.down()
    if type == "-":
        if prev == cur.left():
            return cur.right()
        if prev == cur.right():
            return cur.left()
    if type == "7":
        if prev == cur.left():
            return cur.down()
        if prev == cur.down():
            return cur.left()
    if type == "|":
        if prev == cur.up():
            return cur.down()
        if prev == cur.down():
            return cur.up()
    if type == "L":
        if prev == cur.up():
            return cur.right()
        if prev == cur.right():
            return cur.up()
    if type == "J":
        if prev == cur.left():
            return cur.up()
        if prev == cur.up():
            return cur.left()
