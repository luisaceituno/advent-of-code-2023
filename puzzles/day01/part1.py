from utils.read_input import read_input

lines = read_input()

def extract_num(line: str):
    digits = [char for char in line if char.isdigit()]
    return int(digits[0] + digits[-1])

line_nums = map(extract_num, lines)
total_sum = sum(line_nums)

print(total_sum)

