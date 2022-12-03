def calculate(lines, part):
    sum = 0
    for line in lines:
        item_type = _get_shared_item_type(line)
        sum += _priorities[item_type]
    return sum

def _get_shared_item_type(line):
    partition_at = int(len(line)/2)
    first = line[0:partition_at]
    second = line[partition_at:]
    for char_first in first:
        for char_second in second:
            if char_first == char_second:
                return char_first

_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
_priorities = {c: i + 1 for i, c in enumerate(_chars)}