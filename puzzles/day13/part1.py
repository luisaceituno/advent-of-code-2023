from utils.lists import split_by
from utils.read_input import read_input
from utils.str_processing import transpose


def line_to_bin(line: str):
    bin = "".join(str(".#".index(c)) for c in line)
    return bin


def reflection_point(items: list):
    mirror = list(reversed(items))
    for i in range(1, len(items) - 1):
        max_len = min(i, len(items) - i)
        sub_orig = items[i - max_len : i]
        sub_mirr = mirror[-i - max_len : -i]
        if sub_orig == sub_mirr:
            return i
    return 0


lines = read_input()
groups = list(split_by(lines, lambda l: l == ""))

verticals = 0
horizontals = 0

for group in groups:
    bins_h = [line_to_bin(line) for line in group]
    nums_h = [int(bin, 2) for bin in bins_h]
    h_point = reflection_point(nums_h)
    horizontals += h_point
    if not h_point:
        bins_v = transpose(bins_h)
        nums_v = [int(bin, 2) for bin in bins_v]
        verticals += reflection_point(nums_v)

print(100 * horizontals + verticals)
