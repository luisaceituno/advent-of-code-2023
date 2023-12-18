import re
from utils.coordinates import DOWN, RIGHT, UP, LEFT, YX
from utils.read_input import read_input


lines = read_input()
corners: list[YX] = [YX(0, 0)]
pattern = re.compile(r"^(.) (\d+) \(#(\w+)\)$")
dirs = {"R": RIGHT, "L": LEFT, "U": UP, "D": DOWN}

for line in lines:
    dir_key, length, color = pattern.search(line).groups()
    dir = dirs[dir_key]
    corners.append(corners[-1].move(dir, int(length)))

area = 0
border = 0
for i in range(len(corners)):
    (y1, x1) = corners[i]
    (y2, x2) = corners[(i + 1) % len(corners)]
    area += (x1 * y2) - (x2 * y1)
    border += abs(x2 - x1 + y2 - y1)

print(area / 2 + border / 2 + 1)
