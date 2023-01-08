from enum import IntEnum

def calculate(lines, part):
    grid = [list(map(int, list(line))) for line in lines]
    maxima = {}
    visible_trees = set()
    for i, dimension, line in _get_tree_positions(len(grid)):
        max_height_for_dimension = maxima.get((i, dimension)) or -1
        max_height = -1
        for row, column in line:
            current_height = grid[row][column]
            if current_height == max_height_for_dimension:
                break
            if current_height > max_height:
                visible_trees.add((row, column))
                max_height = current_height
    return len(visible_trees)

def _get_tree_positions(length):
    indexes = list(range(length))
    indexes_reversed = list(reversed(indexes))
    for i in indexes:
        yield i, Dimension.ROW, ((j, i) for j in indexes)
        yield i, Dimension.COLUMN, ((i, j) for j in indexes)
        yield i, Dimension.ROW, ((j, i) for j in indexes_reversed)
        yield i, Dimension.COLUMN, ((i, j) for j in indexes_reversed)

class Dimension(IntEnum):
    ROW = 1,
    COLUMN = 2