import re
from typing import Tuple
from utils.read_input import read_input
from utils.str_processing import int_tokens

Part = Tuple[int, int, int, int]
part_idx = {"x": 0, "m": 1, "a": 2, "s": 3}

lines = read_input()
workflows_strs = lines[: lines.index("")]
parts_strs = lines[lines.index("") + 1 :]

workflow_pattern = re.compile(r"(\w+)\{([^\}]+)\}")
workflows: dict[str, list[str]] = {}
for workflow_str in workflows_strs:
    key, rules_str = workflow_pattern.search(workflow_str).groups()
    rules = rules_str.split(",")
    workflows[key] = rules

parts: list[Part] = [int_tokens(part) for part in parts_strs]
accepted: list[Part] = []

for part in parts:
    workflow_key = "in"
    while workflow_key not in "AR":
        workflow = workflows[workflow_key]
        workflow_key = "R"
        for step in workflow:
            if ":" not in step:
                workflow_key = step
                break
            rule, target = step.split(":")
            component, op, n = rule[0], rule[1], int(rule[2:])
            part_val = part[part_idx[component]]
            if op == "<" and part_val < n or op == ">" and part_val > n:
                workflow_key = target
                break
    if workflow_key == "A":
        accepted.append(part)

score = sum(sum(part) for part in accepted)
print(score)
