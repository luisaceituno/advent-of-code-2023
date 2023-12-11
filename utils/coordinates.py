from dataclasses import dataclass


@dataclass(frozen=True)
class YX:
    y: int
    x: int

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
