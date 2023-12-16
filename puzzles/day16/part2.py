from itertools import repeat
from puzzles.day16.common import Tiles, reflections
from utils.coordinates import YX, down, left, right, up
from utils.read_input import read_input

diagram = read_input()
moves = {"u": up, "r": right, "d": down, "l": left}
starting_points: dict[str, list[tuple[int, int]]] = {
    "r": zip(range(0, len(diagram)), repeat(0)),
    "l": zip(range(0, len(diagram)), repeat(len(diagram[0]) - 1)),
    "u": zip(repeat(len(diagram) - 1), range(0, len(diagram[0]))),
    "d": zip(repeat(0), range(0, len(diagram[0]))),
}

optimal = 0
for entry_dir, entry_points in starting_points.items():
    for entry_point in entry_points:
        tiles: Tiles = {entry_point: [entry_dir]}
        changed: Tiles = tiles.copy()
        while changed:
            to_process = changed.items()
            changed = {}
            for (y, x), beam_dirs in to_process:
                for beam_dir in beam_dirs:
                    next_dirs = reflections[diagram[y][x]][beam_dir]
                    for next_dir in next_dirs:
                        yy, xx = moves[next_dir](y, x)
                        if not YX(yy, xx).is_in(diagram):
                            continue
                        tile_dirs = tiles.setdefault((yy, xx), [])
                        if next_dir not in tile_dirs:
                            tile_dirs.append(next_dir)
                            changed.setdefault((yy, xx), []).append(next_dir)
        optimal = max(optimal, len(tiles))

print(optimal)
