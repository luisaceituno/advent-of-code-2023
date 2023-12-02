from dataclasses import dataclass
from utils.read_input import read_input


@dataclass
class Hand:
    red: int = 0
    green: int = 0
    blue: int = 0


@dataclass
class Game:
    id: int
    hands: list[Hand]


def parse_games(lines: list[str]):
    games: list[Game] = []
    for line in lines:
        [game_str, hands_str] = line.removeprefix("Game ").split(":")
        game = Game(id=int(game_str), hands=[])
        games.append(game)
        for hand_str in hands_str.strip().split("; "):
            colors = {}
            for color_str in hand_str.split(", "):
                [amount, color] = color_str.split(" ")
                colors[color] = int(amount)
            hand = Hand(**colors)
            game.hands.append(hand)
    return games


def read_games():
    lines = read_input()
    return parse_games(lines)
