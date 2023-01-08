from enum import IntEnum

def calculate(lines, part):
    grid = [list(map(int, list(line))) for line in lines]
    match part:
        case 1:
            return _calculate_part_1(grid)
        case 2:
            return _calculate_part_2(grid)

def _calculate_part_1(grid):
    maxima = {}
    visible_trees = set()
    for i, dimension, line in _get_tree_positions_part_1(len(grid)):
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

def _calculate_part_2(grid):
    size = len(grid)
    indexes = list(range(size))
    max_score = 0
    for row in indexes:
        for column in indexes:
            current_height = grid[row][column]
            current_scores = {Direction.UP: 0,  Direction.DOWN: 0, Direction.LEFT: 0, Direction.RIGHT: 0}
            for direction, offsets in _get_tree_positions_part_2(row, column, size):
                for offset_row, offset_column in offsets:
                    offset_height = grid[offset_row][offset_column]
                    direction_score = current_scores[direction]
                    current_scores[direction] = direction_score + 1
                    if offset_height >= current_height:
                        break
            current_score = current_scores[Direction.UP] * current_scores[Direction.DOWN] \
                * current_scores[Direction.LEFT] * current_scores[Direction.RIGHT]
            if current_score > max_score:
                max_score = current_score
    return max_score


def _get_tree_positions_part_1(length):
    indexes = list(range(length))
    indexes_reversed = list(reversed(indexes))
    for i in indexes:
        yield i, Dimension.ROW, ((j, i) for j in indexes)
        yield i, Dimension.COLUMN, ((i, j) for j in indexes)
        yield i, Dimension.ROW, ((j, i) for j in indexes_reversed)
        yield i, Dimension.COLUMN, ((i, j) for j in indexes_reversed)

def _get_tree_positions_part_2(row, column, size):
    yield Direction.UP, ((row1, column) for row1 in range(row - 1, -1, -1))
    yield Direction.DOWN, ((row1, column) for row1 in range(row + 1, size))
    yield Direction.LEFT, ((row, column1) for column1 in range(column - 1, -1, -1))
    yield Direction.RIGHT, ((row, column1) for column1 in range(column + 1, size))

class Dimension(IntEnum):
    ROW = 1,
    COLUMN = 2

class Direction(IntEnum):
    UP = 1,
    DOWN = 2,
    LEFT = 3,
    RIGHT = 4