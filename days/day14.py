def calculate(lines, part):
    pass

def parse_paths(lines):
    paths = []
    min = 0
    max = 0
    max_y = 0
    for line in lines:
        path = []
        items = line.split('->')
        for item in items:
            left, _, right = item.strip().partition(',')
            int_left = int(left)
            if min == 0 or min > int_left:
                min = int_left
            if max == 0 or max < int_left:
                max = int_left
            int_right = int(right)
            if max_y == 0 or max_y < int_right:
                max_y = int_right
            path.append((int_left, int_right))
        paths.append(path)
    return paths, min, max, max_y
