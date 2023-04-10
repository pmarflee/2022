from functools import cmp_to_key
from itertools import zip_longest

def calculate(lines, part):
    packets = __get_packets(lines)
    match part:
        case 1:
            return __calculate_part1(packets)
        case 2:
            return __calculate_part2(packets)
        case _:
            raise ValueError('Invalid part')

def __calculate_part1(packets):
    return sum((i + 1 for i, pair in enumerate(__get_pairs(packets)) \
                if __compare(*pair) == -1))

def __calculate_part2(packets):
    dividers = [[2], [6]]
    packets.extend(dividers)
    packets.sort(key=cmp_to_key(__compare))
    indexes = [packets.index(d) + 1 for d in dividers]

    return indexes[0] * indexes[1]

def __get_packets(lines):
    return [eval(line) for line in lines if line != '']

def __get_pairs(packets):
    return ((packets[step], packets[step + 1]) \
            for step in range(0, len(packets) - 1, 2))

def __compare(left, right):
    if left == None:
        return -1
    if right == None:
        return 1

    type_left = type(left)
    type_right = type(right)

    if type_left is int and type_right is int:
        if left < right:
            return -1
        if left > right:
            return 1
        return 0

    for pair in zip_longest(__to_list(left), __to_list(right)):
        result = __compare(*pair)
        if result != 0:
            return result

    return 0

def __to_list(value):
    return value if type(value) is list else [value]

