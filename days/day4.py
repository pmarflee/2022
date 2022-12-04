import re

def calculate(lines, part):
    count = 0
    for line in lines:
        first_from, first_to, second_from, second_to = _parse(line) 
        if first_to - first_from > second_to - second_from:
            if _contains(first_from, first_to, second_from, second_to):
                count += 1
        elif _contains(second_from, second_to, first_from, first_to):
            count += 1
    return count

def _parse(line):
    m = _regex.match(line)
    return int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))

def _contains(larger_from, larger_to, smaller_from, smaller_to):
    return smaller_from >= larger_from and smaller_to <= larger_to

_regex = re.compile(r"^(\d+)-(\d+),(\d+)-(\d+)$")