from puzzles.day04.common import Card, parse_card
from utils.read_input import read_input


lines = read_input()
cards = [parse_card(line) for line in lines]
initial_count = len(cards)
multipliers = {}

for card in cards:
    multiplier = 1 + multipliers.get(card.id, 0)
    winners = card.winners_count()
    for i in range(0, winners):
        cur_id = card.id + i + 1
        multipliers[cur_id] = multipliers.setdefault(cur_id, 0) + multiplier

total_cards = initial_count + sum(multipliers.values())
print(total_cards)
