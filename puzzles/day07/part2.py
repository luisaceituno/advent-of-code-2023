from puzzles.day07.common import Game, hand_class
from utils.read_input import read_input


def hand_strength(hand: str):
    hexed = "".join([hex_transforms.get(c, c) for c in hand])
    class_str = str(hand_class(hand, apply_joker=True))
    return int(class_str + hexed, base=16)


lines = read_input()

hex_transforms = {"T": "a", "J": "1", "Q": "c", "K": "d", "A": "e"}

games = [
    Game(hand, int(bet), hand_strength(hand))
    for hand, bet in (line.split() for line in lines)
]
ranked = sorted(games, key=lambda g: g.strength)
winnings = sum(game.bet * (i + 1) for i, game in enumerate(ranked))
print(winnings)
