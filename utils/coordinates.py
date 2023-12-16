from typing import Self


class YX(tuple):
    def __new__(cls, y: int, x: int) -> Self:
        return super().__new__(cls, (y, x))

    def __init__(self, y: int, x: int) -> None:
        super().__init__()
        self.y = y
        self.x = x

    def up(self):
        return YX(self.y - 1, self.x)

    def right(self):
        return YX(self.y, self.x + 1)

    def down(self):
        return YX(self.y + 1, self.x)

    def left(self):
        return YX(self.y, self.x - 1)

    def cross(self):
        return [self.up(), self.right(), self.down(), self.left()]

    def is_in(self, map: list[list]):
        return (
            self.x >= 0
            and self.y >= 0
            and self.y < len(map)
            and self.x < len(map[self.y])
        )

    def on(self, map: list[list]):
        return map[self.y][self.x]

    def dist_manhattan(self, other: Self):
        return abs(other.y - self.y) + abs(other.x - self.x)

    def range_y(self, other: Self):
        s, e = sorted([self.y, other.y])
        return range(s, e)

    def range_x(self, other: Self):
        s, e = sorted([self.x, other.x])
        return range(s, e)


def up(y: int, x: int):
    return YX(y, x).up()


def right(y: int, x: int):
    return YX(y, x).right()


def down(y: int, x: int):
    return YX(y, x).down()


def left(y: int, x: int):
    return YX(y, x).left()
