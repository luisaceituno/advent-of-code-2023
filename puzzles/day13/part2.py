from utils.lists import diff_elems, split_by
from utils.read_input import read_input
from utils.str_processing import transpose


def line_to_bin(line: str):
    bin = "".join(str(".#".index(c)) for c in line)
    return bin


def can_correct_with_bit_flip(a: int, b: int):
    diff_bits = a ^ b
    # diff is power of 2, represents a single bit having value 1
    return (diff_bits & (diff_bits - 1)) == 0


def reflection_point_corrected(items: list):
    mirror = list(reversed(items))
    for i in range(1, len(items)):
        max_len = min(i, len(items) - i)
        sub_orig = items[i - max_len : i]
        sub_mirr = mirror[-i - max_len : -i]
        diffs = list(diff_elems(sub_orig, sub_mirr))
        if len(diffs) == 1 and can_correct_with_bit_flip(*(diffs[0])):
            return i
    return 0


lines = read_input()
groups = list(split_by(lines, lambda l: l == ""))

verticals = 0
horizontals = 0

for group in groups:
    bins_h = [line_to_bin(line) for line in group]
    nums_h = [int(bin, 2) for bin in bins_h]
    h_point = reflection_point_corrected(nums_h)
    horizontals += h_point
    if h_point == 0:
        bins_v = transpose(bins_h)
        nums_v = [int(bin, 2) for bin in bins_v]
        v_point = reflection_point_corrected(nums_v)
        verticals += v_point

print(100 * horizontals + verticals)
