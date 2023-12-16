from puzzles.day16.common import Tiles, reflections
from utils.coordinates import YX, down, left, right, up
from utils.read_input import read_input

diagram = read_input()
moves = {"u": up, "r": right, "d": down, "l": left}
tiles: Tiles = {(0, 0): ["r"]}
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

print(len(tiles))
