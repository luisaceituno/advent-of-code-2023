from typing import NamedTuple, Self


class Direction(NamedTuple):
    clock: int
    y: int
    x: int

    def right(self):
        return DIRECTIONS[(self.clock + 3) % 12]

    def left(self):
        return DIRECTIONS[(self.clock - 3) % 12]


UP = Direction(0, -1, 0)
RIGHT = Direction(3, 0, 1)
DOWN = Direction(6, 1, 0)
LEFT = Direction(9, 0, -1)

DIRECTIONS = {0: UP, 3: RIGHT, 6: DOWN, 9: LEFT}


class YX(NamedTuple):
    y: int
    x: int

    def move(self, dir: Direction, steps=1):
        return YX(self.y + dir.y * steps, self.x + dir.x * steps)

    def cross(self):
        return [self.move(dir) for dir in DIRECTIONS.values()]

    def is_in(self, map: list[list]):
        return (
            self.x >= 0
            and self.y >= 0
            and self.y < len(map)
            and self.x < len(map[self.y])
        )

    def on[T](self, map: list[list[T]]):
        return map[self.y][self.x]

    def on_wrapped[T](self, map: list[list[T]]):
        y = self.y % len(map)
        x = self.x % len(map[y])
        return YX(y, x).on(map)

    def dist_manhattan(self, other: Self):
        return abs(other.y - self.y) + abs(other.x - self.x)

    def range_y(self, other: Self):
        s, e = sorted([self.y, other.y])
        return range(s, e)

    def range_x(self, other: Self):
        s, e = sorted([self.x, other.x])
        return range(s, e)
