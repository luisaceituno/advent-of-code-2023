from puzzles.day02.common import Game, read_games


def is_possible(game: Game, max_red: int, max_green: int, max_blue: int):
    hand_results = map(
        lambda hand: hand.red <= max_red
        and hand.green <= max_green
        and hand.blue <= max_blue,
        game.hands,
    )
    return all(hand_results)


games = read_games()
sum_ids = sum(game.id for game in games if is_possible(game, 12, 13, 14))
print(sum_ids)
