import re
from puzzles.day15.common import ascii_hash
from utils.read_input import read_input

sequence = read_input()[0]
steps = sequence.split(",")
boxes: dict[int, dict[str, int]] = {}  # box_num -> (lens_label -> focal_length)
pattern = re.compile(r"^([a-zA-Z]+)([=-])(\d+)?$")

for step in steps:
    label, action, focal_length = pattern.search(step).groups()
    box_num = ascii_hash(label)
    boxes.setdefault(box_num, {})
    box = boxes[box_num]
    if action == "-":
        box.pop(label, None)
    else:
        box[label] = int(focal_length)

sum_powers = 0
for box_num, lenses in boxes.items():
    for lens_slot, (label, focal_length) in enumerate(lenses.items(), 1):
        sum_powers += (box_num + 1) * lens_slot * focal_length

print(sum_powers)
