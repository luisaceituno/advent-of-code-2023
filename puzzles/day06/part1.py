import re
from puzzles.day06.common import press_min_max
from utils.read_input import read_input

lines = read_input()

times = [int(num) for num in re.split(r"\s+", lines[0].replace("Time:", "")) if num]
distances = [
    int(num) for num in re.split(r"\s+", lines[1].replace("Distance:", "")) if num
]

acc = 1

for i in range(len(times)):
    min_press, max_press = press_min_max(times[i], distances[i])
    diff = max_press - min_press + 1
    acc *= int(diff)

print(acc)
