import re
import timeit
from utils.read_input import read_input
from utils.str_processing import int_tokens


def fit_next(criteria: str, groups: list[int]):
    if len(groups) == 0:
        if "#" in criteria:
            return 0
        return 1
    cur_sum = 0
    cur, remaining = groups[0], groups[1:]
    for i in range(0, len(criteria) - (sum(remaining) + len(remaining) - 1)):
        pattern = criteria[i : i + cur]
        if len(pattern) < cur:
            break
        if all([c in "?#" for c in pattern]):
            if criteria[i + cur : i + cur + 1] == "#":
                continue
            cur_sum += fit_next(criteria[i + cur + 1 :], remaining)
        if pattern[0] == "#":
            break
    return cur_sum


input = read_input()
total_sum = 0
for line in input:
    criteria_str, groups_str = line.split()
    groups = int_tokens(groups_str)
    clean_criteria = re.sub(r"\.+", ".", criteria_str)
    total_sum += fit_next(clean_criteria, groups)

print(total_sum)
