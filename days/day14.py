def calculate(lines, part):
    pass

def parse_lines(lines):
    paths = []
    for line in lines:
        path = []
        items = line.split('->')
        for item in items:
            left, _, right = item.strip().partition(',')
            path.append((int(left), int(right)))
        paths.append(path)
    return paths
