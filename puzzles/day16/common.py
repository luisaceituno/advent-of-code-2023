reflections = {
    ".": {"u": ["u"], "r": ["r"], "d": ["d"], "l": ["l"]},
    "\\": {"u": ["l"], "r": ["d"], "d": ["r"], "l": ["u"]},
    "/": {"u": ["r"], "r": ["u"], "d": ["l"], "l": ["d"]},
    "-": {"u": ["l", "r"], "r": ["r"], "d": ["l", "r"], "l": ["l"]},
    "|": {"u": ["u"], "r": ["u", "d"], "d": ["d"], "l": ["u", "d"]},
}
Dir = str  # u, r, d, l
Coord = tuple[int, int]
Tiles = dict[Coord, list[Dir]]
