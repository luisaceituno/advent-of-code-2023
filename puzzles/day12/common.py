def fit_next(criteria: str, groups: list[int], cache: dict, pos=(0, 0)):
    if len(groups) == 0:
        if "#" in criteria:
            return 0
        return 1
    if pos in cache:
        return cache.get(pos)
    cur_sum = 0
    cur, remaining = groups[0], groups[1:]
    for i in range(0, len(criteria) - (sum(remaining) + len(remaining) - 1)):
        pattern = criteria[i : i + cur]
        if len(pattern) < cur:
            break
        if all(c in "?#" for c in pattern):
            if criteria[i + cur : i + cur + 1] != "#":
                next_pos = (pos[0] + i + cur + 1, pos[1] + 1)
                cur_sum += fit_next(criteria[i + cur + 1 :], remaining, cache, next_pos)
        if pattern[0] == "#":
            break
    cache[pos] = cur_sum
    return cur_sum
