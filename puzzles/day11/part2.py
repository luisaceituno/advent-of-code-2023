from utils.coordinates import YX
from utils.lists import filter_2d
from utils.read_input import read_input

input = read_input()

empty_rows = {*range(len(input))}
empty_cols = {*range(len(input[0]))}

stars: list[YX] = []

for star, y, x in filter_2d(input, lambda s: s == "#"):
    stars.append(YX(y, x))
    empty_rows.discard(y)
    empty_cols.discard(x)

sum = 0

for i, star_a in enumerate(stars):
    for j in range(i):
        star_b = stars[j]
        sum += star_a.dist_manhattan(star_b)
        ys = star_a.range_y(star_b)
        xs = star_a.range_x(star_b)
        sum += 999999 * len(empty_rows.intersection(ys))
        sum += 999999 * len(empty_cols.intersection(xs))

print(sum)
