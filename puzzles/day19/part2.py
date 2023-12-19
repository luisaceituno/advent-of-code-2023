from math import prod
from queue import Queue
import re
from typing import Tuple
from utils.read_input import read_input


def split_range(r: range, op: str, n: int):
    if op == "<":
        return range(r.start, n), range(n, r.stop)
    else:
        return range(n + 1, r.stop), range(r.start, n + 1)


PartGroup = Tuple[str, range, range, range, range]
part_idx = {"x": 0, "m": 1, "a": 2, "s": 3}

lines = read_input()
workflows_strs = lines[: lines.index("")]

workflow_pattern = re.compile(r"(\w+)\{([^\}]+)\}")
workflows: dict[str, list[str]] = {}
for workflow_str in workflows_strs:
    key, rules_str = workflow_pattern.search(workflow_str).groups()
    rules = rules_str.split(",")
    workflows[key] = rules

q = Queue[PartGroup]()
q.put(("in", range(1, 4001), range(1, 4001), range(1, 4001), range(1, 4001)))
combinations = 0
while not q.empty():
    (key, *components) = q.get()
    if key == "A":
        combinations += prod(len(c) for c in components)
        continue
    elif key == "R":
        continue
    for step in workflows[key]:
        if step == "A":
            combinations += prod(len(c) for c in components)
        elif ":" in step:
            rule, target = step.split(":")
            component, op, n = rule[0], rule[1], int(rule[2:])
            next_components = components.copy()
            idx = part_idx[component]
            component_range = next_components[idx]
            next_range, remaining = split_range(component_range, op, n)
            next_components[idx] = next_range
            if next_range:
                q.put((target, *next_components))
            if not remaining:
                break
            components[idx] = remaining
        elif step != "R":
            q.put((step, *components))

print(combinations)
