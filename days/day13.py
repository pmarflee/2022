from itertools import zip_longest

def calculate(lines, part):
    sum = 0

    for i, step in enumerate(range(0, len(lines) - 1, 3)):
        left = eval(lines[step])
        right = eval(lines[step + 1])
        if compare(left, right):
            sum += i + 1
                
    return sum

def compare(left, right):
    if left == None:
        return True
    if right == None:
        return False

    type_left = type(left)
    type_right = type(right)

    if type_left is int and type_right is int:
        if left < right:
            return True
        if left > right:
            return False
        return None

    if type_left is not list:
        left = [left] 
    elif type_right is not list:
        right = [right]

    for pair in zip_longest(left, right):
        result = compare(*pair)
        if result is not None:
            return result

