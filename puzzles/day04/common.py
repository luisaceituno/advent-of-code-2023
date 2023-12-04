from dataclasses import dataclass
import re


@dataclass(frozen=True)
class Card:
    id: int
    winners: list[int]
    current: list[int]

    def winners_count(self):
        return sum(1 for winner in self.current if winner in self.winners)


def parse_card(line: str):
    card_str, nums_str = line.split(":")
    card_num = int(re.sub(r"Card\s+", "", card_str))
    winners_str, currents_str = nums_str.split("|")
    winners = [int(winner) for winner in re.split(r"\s+", winners_str.strip())]
    currents = [int(current) for current in re.split(r"\s+", currents_str.strip())]
    return Card(card_num, winners, currents)
