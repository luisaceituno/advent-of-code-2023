from puzzles.day03.common import EMPTY_SYMBOL, find_parts_by_symbol
from utils.lists import multiply
from utils.read_input import read_input


lines = read_input()
parts_by_symbol = find_parts_by_symbol(lines)

result = sum(
    multiply(*parts_by_symbol[symbol])
    for symbol in parts_by_symbol
    if symbol.char == "*" and len(parts_by_symbol[symbol]) == 2
)
print(result)
