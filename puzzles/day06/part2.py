import re
from puzzles.day06.common import press_min_max
from utils.read_input import read_input

lines = read_input()

time = int(re.sub(r"\s+", "", lines[0].replace("Time:", "")))
distance = int(re.sub(r"\s+", "", lines[1].replace("Distance:", "")))

min_press, max_press = press_min_max(time, distance)
diff = max_press - min_press + 1

print(diff)
