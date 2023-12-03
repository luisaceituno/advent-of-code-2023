from dataclasses import dataclass
from utils.str_processing import chars_surrounding


@dataclass(frozen=True)
class Symbol:
    char: str
    y: int
    x: int


EMPTY_SYMBOL = Symbol("", -1, -1)


def find_symbol_surrounding(lines: list[str], y: int, x: int):
    return next(
        (
            Symbol(char, char_y, char_x)
            for char, char_y, char_x in chars_surrounding(lines, y, x)
            if char != "." and not char.isdigit()
        ),
        EMPTY_SYMBOL,
    )


def find_parts_by_symbol(lines: list[str]):
    parts_by_symbol: dict[Symbol, list[int]] = {}
    for line_idx, line in enumerate(lines):
        last_digits = ""
        last_symbol = EMPTY_SYMBOL
        for char_idx, char in enumerate(line + "."):
            if char.isdigit():
                last_digits += char
                if last_symbol == EMPTY_SYMBOL:
                    last_symbol = find_symbol_surrounding(lines, line_idx, char_idx)
            elif last_digits != "":
                if last_symbol not in parts_by_symbol:
                    parts_by_symbol[last_symbol] = []
                parts_by_symbol[last_symbol].append(int(last_digits))
                last_digits = ""
                last_symbol = EMPTY_SYMBOL
    return parts_by_symbol
