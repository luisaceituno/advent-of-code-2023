from puzzles.day03.common import EMPTY_SYMBOL, find_parts_by_symbol
from utils.read_input import read_input


lines = read_input()
parts_by_symbol = find_parts_by_symbol(lines)

sum_parts_with_symbol = sum(
    sum(parts_by_symbol[symbol]) for symbol in parts_by_symbol if symbol != EMPTY_SYMBOL
)
print(sum_parts_with_symbol)
