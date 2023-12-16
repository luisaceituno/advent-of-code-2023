def ascii_hash(s: str):
    cur = 0
    for c in s:
        cur = (cur + ord(c)) * 17 % 256
    return cur
