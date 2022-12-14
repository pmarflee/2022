def calculate(buffer, part):
    i = 0
    segment_size = 4 if part == 1 else 14
    while True:
        if len({c for c in buffer[i:i+segment_size]}) == segment_size:
            return i + segment_size
        i += 1