def calculate(lines, part):
    match part:
        case 1:
            return calculate_part_1(lines)
        case 2:
            return calculate_part_2(lines)

def calculate_part_1(lines):
    sum = 0
    for line in lines:
        item_type = _get_shared_item_type(line)
        sum += _priorities[item_type]
    return sum

def calculate_part_2(lines):
    sum = 0
    for first, second, third in _get_groups(lines, 3):
        badge = _get_badge(first, second, third)
        sum += _priorities[badge]
    return sum

def _get_shared_item_type(line):
    partition_at = int(len(line)/2)
    first = line[0:partition_at]
    second = line[partition_at:]
    for char_first in first:
        for char_second in second:
            if char_first == char_second:
                return char_first

def _get_groups(lines, size):
    for i in range(0, len(lines), size):
        yield tuple(lines[i:i + size])

def _get_badge(first, second, third):
    for char_first in first:
        for char_second in second:
            for char_third in third:
                if char_first == char_second and char_second == char_third:
                    return char_first

_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
_priorities = {c: i + 1 for i, c in enumerate(_chars)}