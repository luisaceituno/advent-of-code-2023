from puzzles.day02.common import Game, read_games


def cubeset_power(red: int = 0, green: int = 0, blue: int = 0):
    return red * green * blue


def min_cubeset(game: Game):
    red_hands = filter(lambda hand: hand.red > 0, game.hands)
    green_hands = filter(lambda hand: hand.green > 0, game.hands)
    blue_hands = filter(lambda hand: hand.blue > 0, game.hands)
    return {
        "red": max(hand.red for hand in red_hands),
        "green": max(hand.green for hand in green_hands),
        "blue": max(hand.blue for hand in blue_hands),
    }


games = read_games()
sum_powers = sum(cubeset_power(**cubeset) for cubeset in map(min_cubeset, games))
print(sum_powers)
