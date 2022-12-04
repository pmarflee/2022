import re

def calculate(lines, part):
    count = 0
    for line in lines:
        set_first, set_second = _parse(line) 
        if (part == 1 and (set_first.issubset(set_second) or set_second.issubset(set_first))) or (part ==2 and (not set_first.isdisjoint(set_second) or not set_second.isdisjoint(set_first))):
            count += 1 
    return count

def _parse(line):
    m = _regex.match(line)
    return set(range(int(m.group(1)), int(m.group(2)) + 1)), set(range(int(m.group(3)), int(m.group(4)) + 1))

_regex = re.compile(r"^(\d+)-(\d+),(\d+)-(\d+)$")