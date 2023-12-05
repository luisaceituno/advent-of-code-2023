from puzzles.day05.common import parse_almanac
from utils.read_input import read_input

lines = read_input()
almanac = parse_almanac(lines)

lowest = min(almanac.find_for_seed(seed, "location") for seed in almanac.seeds)
print(lowest)
