def tryParseInt(s, base=10):
    try:
        return int(s, base), True
    except ValueError:
        return 0, False