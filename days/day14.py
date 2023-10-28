from dataclasses import dataclass
from enum import Enum
from itertools import pairwise
from typing import Optional


@dataclass
class ScanResult:
    paths: list[list[tuple[int, int]]]
    min_x: int
    max_x: int
    max_y: int


class Stuff(Enum):
    ROCK = 1
    SAND = 2
    SOURCE = 3


class Cave:
    def __init__(self, scan: ScanResult):
        self.__offset = scan.min_x
        self.__source = (0, 500 - scan.min_x)

        width = scan.max_x - scan.min_x
        self.__data: list[list[Optional[Stuff]]] = [[None for _ in range(width + 1)] for _ in range(scan.max_y + 1)]

        for line in scan.paths:
            for (x_previous, y_previous), (x_current, y_current) in pairwise(line):
                for x, y in self.__get_rock_range(x_previous, y_previous, x_current, y_current):
                    self.__set_stuff(x, y, Stuff.ROCK)

        self.__set_stuff(self.__source[1], self.__source[0], Stuff.SOURCE)
        self.__width = width

    @property
    def data(self):
        return self.__data

    def __get_row_index(self, x: int) -> int:
        return x - self.__offset

    def __get_rock_range(self, x_previous: int, y_previous: int, x_current: int, y_current: int) -> list[tuple[int, int]]:
        if x_previous == x_current:
            x = self.__get_row_index(x_previous)
            min_y, max_y = min(y_previous, y_current), max(y_previous, y_current)
            return [(x, y) for y in range(min_y, max_y + 1)]
        else:
            min_x, max_x = min(x_previous, x_current), max(x_previous, x_current)
            return [(self.__get_row_index(x), y_previous) for x in range(min_x, max_x + 1)]

    def __set_stuff(self, x: int, y: int, stuff: Stuff):
        self.__data[y][x] = stuff

def calculate(lines, part):
    pass


def parse_paths(lines):
    paths = []
    min_x = 0
    max_x = 0
    max_y = 0
    for line in lines:
        path = []
        items = line.split('->')
        for item in items:
            left, _, right = item.strip().partition(',')
            int_left = int(left)
            if min_x == 0 or min_x > int_left:
                min_x = int_left
            if max_x == 0 or max_x < int_left:
                max_x = int_left
            int_right = int(right)
            if max_y == 0 or max_y < int_right:
                max_y = int_right
            path.append((int_left, int_right))
        paths.append(path)
    return ScanResult(paths=paths, min_x=min_x, max_x=max_x, max_y=max_y)
