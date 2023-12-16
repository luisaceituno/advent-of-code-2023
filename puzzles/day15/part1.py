from puzzles.day15.common import ascii_hash
from utils.read_input import read_input


sequence = read_input()[0]
steps = sequence.split(",")

sum = 0
for step in steps:
    sum += ascii_hash(step)

print(sum)
