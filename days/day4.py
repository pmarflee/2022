import re

def calculate(lines, part):
    count = 0
    for line in lines:
        set_first, set_second = _parse(line) 
        match part:
            case 1:
                if set_first.issubset(set_second) or set_second.issubset(set_first):
                    count += 1 
            case 2:
                if not set_first.isdisjoint(set_second) or not set_second.isdisjoint(set_first):
                    count += 1
    return count

def _parse(line):
    m = _regex.match(line)
    return set([i for i in range(int(m.group(1)), int(m.group(2)) + 1)]), set([i for i in range(int(m.group(3)), int(m.group(4)) + 1)])

_regex = re.compile(r"^(\d+)-(\d+),(\d+)-(\d+)$")