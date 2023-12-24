from typing import NamedTuple
from utils.math import sign


class ZYX(NamedTuple):
    z: int
    y: int
    x: int

    def direction_to(self, other):
        dz = sign(other.z - self.z)
        dy = sign(other.y - self.y)
        dx = sign(other.x - self.x)
        return ZYX(dz, dy, dx)
