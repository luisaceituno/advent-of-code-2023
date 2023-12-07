from dataclasses import dataclass


@dataclass
class Game:
    hand: str
    bet: int
    strength: int


class_by_combos = {
    (5,): 7,
    (1, 4): 6,
    (2, 3): 5,
    (1, 1, 3): 4,
    (1, 2, 2): 3,
    (1, 1, 1, 2): 2,
    (1, 1, 1, 1, 1): 1,
}


def hand_class(hand: str, apply_joker: bool = False):
    base_counts: dict[str, int] = {}
    for card in hand:
        base_counts.setdefault(card, 0)
        base_counts[card] += 1

    joker_counts = base_counts.copy()
    if apply_joker and base_counts.get("J") and len(base_counts) > 1:
        del joker_counts["J"]
        target = max(joker_counts, key=joker_counts.get)[0]
        joker_counts[target] += base_counts.get("J", 0)

    combos = tuple(sorted(base_counts.values()))
    joker_combos = tuple(sorted(joker_counts.values()))
    return max(class_by_combos[combos], class_by_combos[joker_combos])
