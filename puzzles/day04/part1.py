from puzzles.day04.common import Card, parse_card
from utils.read_input import read_input


def card_worth(card: Card):
    winners_count = card.winners_count()
    if winners_count == 0:
        return 0
    return pow(2, winners_count - 1)


lines = read_input()
cards = [parse_card(line) for line in lines]
result = sum(map(card_worth, cards))
print(result)
