from itertools import chain, repeat
import re
from puzzles.day12.common import fit_next
from utils.read_input import read_input
from utils.str_processing import int_tokens

lines = read_input()
total_sum = 0
for line in lines:
    criteria_str, groups_str = line.split()
    groups = int_tokens(groups_str)
    groups_unfolded = list(chain.from_iterable(repeat(groups, 5)))
    criteria = re.sub(r"\.+", ".", criteria_str)
    criteria_unfolded = "?".join(repeat(criteria, 5))
    possibilities = fit_next(criteria_unfolded, groups_unfolded, {})
    total_sum += possibilities

print(total_sum)
