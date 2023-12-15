import re
from puzzles.day12.common import fit_next
from utils.read_input import read_input
from utils.str_processing import int_tokens

lines = read_input()
total_sum = 0
for line in lines:
    criteria_str, groups_str = line.split()
    groups = int_tokens(groups_str)
    clean_criteria = re.sub(r"\.+", ".", criteria_str)
    possibilities = fit_next(clean_criteria, groups, {})
    total_sum += possibilities

print(total_sum)
