from utils.read_input import read_input

lines = read_input()

"""
We use this weird format to allow two digits to share characters. For example
"twone" shares the "o", so both replacing it with "2ne" or "tw1" would be wrong
and miss one digit.
"""
digit_replacements = [
    ["one", "one1one"],
    ["two", "two2two"],
    ["three", "three3three"],
    ["four", "four4four"],
    ["five", "five5five"],
    ["six", "six6six"],
    ["seven", "seven7seven"],
    ["eight", "eight8eight"],
    ["nine", "nine9nine"],
]


def inject_spelled_out_digits(line: str) -> str:
    injected_line = line
    for [number_str, number_val] in digit_replacements:
        injected_line = injected_line.replace(number_str, number_val)
    return injected_line


def extract_num(line: str) -> int:
    line_with_digits = inject_spelled_out_digits(line)
    digits = [char for char in line_with_digits if char.isdigit()]
    return int(digits[0] + digits[-1])


line_nums = map(extract_num, lines)
total_sum = sum(line_nums)

print(total_sum)
