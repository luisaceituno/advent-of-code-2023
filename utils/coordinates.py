from typing import NamedTuple, Self


class YX(NamedTuple):
    y: int
    x: int

    def up(self, steps=1):
        return YX(self.y - steps, self.x)

    def right(self, steps=1):
        return YX(self.y, self.x + steps)

    def down(self, steps=1):
        return YX(self.y + steps, self.x)

    def left(self, steps=1):
        return YX(self.y, self.x - steps)

    def cross(self):
        return [self.up(), self.right(), self.down(), self.left()]

    def is_in(self, map: list[list]):
        return (
            self.x >= 0
            and self.y >= 0
            and self.y < len(map)
            and self.x < len(map[self.y])
        )

    def on[T](self, map: list[list[T]]):
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
