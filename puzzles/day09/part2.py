from utils.read_input import read_input
from utils.str_processing import int_tokens


input = read_input()

seqs = [int_tokens(line) for line in input]

nexts: list[int] = []

for seq in seqs:
    deltas = seq
    dsum = seq[0]
    sign = 1
    while True:
        deltas = [deltas[i] - deltas[i - 1] for i in range(1, len(deltas))]
        dsum -= sign * deltas[0]
        sign = -sign
        if all(d == 0 for d in deltas):
            break
    nexts.append(dsum)

print(sum(nexts))
