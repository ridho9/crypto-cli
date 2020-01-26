def lalpha_ord(c):
    if isinstance(c, int):
        c = chr(c)
    if c.isupper():
        c = c.lower()
    return ord(c) - ord("a")


def is_int_alpha(c):
    return (ord("a") <= c <= ord("z")) or (ord("A") <= c <= ord("Z"))
