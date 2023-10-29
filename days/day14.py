from __future__ import annotations

import string
import os.path

from dataclasses import dataclass
from enum import Enum
from itertools import pairwise
from typing import Optional

enable_logging = False

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


class MoveResult(Enum):
    FALLING = 1
    RESTED = 2
    LOST = 3


class Grain:
    __offsets = [(0, 1), (-1, 1), (1, 1)]

    def __init__(self, cave: Cave):
        self.__location: Optional[tuple[int, int]] = cave.source
        self.__cave = cave

    @property
    def location(self) -> Optional[tuple[int, int]]:
        return self.__location

    @property
    def cave(self):
        return self.__cave

    @property
    def is_lost(self) -> bool:
        return self.location is None

    def drop(self) -> None:
        result = MoveResult.FALLING

        while result == MoveResult.FALLING:
            new_result: Optional[MoveResult] = None

            for x_offset, y_offset in Grain.__offsets:
                if (next_location := self.__check_next_location(x_offset, y_offset)) is None:
                    self.cave.set_stuff(None, *self.__location)
                    self.__location = None
                    new_result = MoveResult.LOST
                    break
                else:
                    next_x, next_y, stuff = next_location

                    if stuff is None:
                        self.cave.move_sand(self.location, (next_x, next_y))
                        self.__location = (next_x, next_y)
                        new_result = MoveResult.FALLING
                        self.cave.log_grain_location(self)
                        break

            result = new_result if new_result is not None else MoveResult.RESTED

    def __can_move_x(self, x_offset: int) -> bool:
        return self.cave.get_stuff(self.location[0] + x_offset, self.location[1]) is None

    def __check_next_location(self, x_offset: int, y_offset: int) -> Optional[tuple[int, int, Optional[Stuff]]]:
        if self.location is None:
            raise TypeError

        location_x, location_y = self.location
        next_x, next_y = location_x + x_offset, location_y + y_offset

        if next_x > self.cave.width or next_x < 0 or next_y > self.cave.height:
            return None

        return next_x, next_y, self.cave.get_stuff(next_x, next_y)


class Cave:
    __log_file = 'day14.txt'

    def __init__(self, scan: ScanResult):
        self.__offset = scan.min_x
        self.__source = (500 - scan.min_x, 0)

        width = scan.max_x - scan.min_x
        self.__data: list[list[Optional[Stuff]]] = [[None for _ in range(width + 1)] for _ in range(scan.max_y + 1)]

        for line in scan.paths:
            for (x_previous, y_previous), (x_current, y_current) in pairwise(line):
                for x, y in self.__get_rock_range(x_previous, y_previous, x_current, y_current):
                    self.set_stuff(Stuff.ROCK, x, y)

        self.set_stuff(Stuff.SOURCE, *self.__source)
        self.__width = width
        self.__height = scan.max_y
        self.__is_full = False
        self.__last_grain = None

    @property
    def data(self):
        return self.__data

    @property
    def source(self):
        return self.__source

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def last_grain(self) -> Optional[Grain]:
        return self.__last_grain

    def produce_sand(self) -> int:
        count = 0
        i = 0

        self.__clear_log()
        self.__log(i)

        while True:
            i += 1
            grain = Grain(self)
            grain.drop()
            if grain.is_lost:
                break
            else:
                self.__last_grain = grain
                self.__log(i)
                count += 1

        return count

    def move_sand(self, from_location: tuple[int, int], to_location: tuple[int, int]):
        if self.get_stuff(*from_location) == Stuff.SAND:
            self.set_stuff(None, *from_location)
        self.set_stuff(Stuff.SAND, *to_location)

    def __str__(self):
        result = '\r\n'

        for row, line in enumerate(self.data):
            for col, stuff in enumerate(line):
                match stuff:
                    case Stuff.ROCK:
                        c = '#'
                    case Stuff.SAND:
                        c = 'O' if self.last_grain is not None and (col, row) == self.last_grain.location else 'o'
                    case Stuff.SOURCE:
                        c = '+'
                    case None:
                        c = '.'

                result += c

            result += '\n'

        return result

    def __get_row_index(self, x: int) -> int:
        return x - self.__offset

    def __get_rock_range(self, x_previous: int, y_previous: int, x_current: int, y_current: int) -> list[
            tuple[int, int]]:
        if x_previous == x_current:
            x = self.__get_row_index(x_previous)
            min_y, max_y = min(y_previous, y_current), max(y_previous, y_current)
            return [(x, y) for y in range(min_y, max_y + 1)]
        else:
            min_x, max_x = min(x_previous, x_current), max(x_previous, x_current)
            return [(self.__get_row_index(x), y_previous) for x in range(min_x, max_x + 1)]

    def set_stuff(self, stuff: Optional[Stuff], x: int, y: int):
        self.__data[y][x] = stuff

    def get_stuff(self, x: int, y: int) -> Optional[Stuff]:
        return self.data[y][x]

    def __log(self, count: int):
        if enable_logging:
            with open(Cave.__log_file, 'a') as log_file:
                log_file.write(f"{count}\n")
                log_file.writelines(f"{self}\n")

    def log_grain_location(self, grain: Grain) -> None:
        if enable_logging:
            with open(Cave.__log_file, 'a') as log_file:
                log_file.write(f"Grain location: {grain.location}\n")

    @staticmethod
    def __clear_log():
        if enable_logging:
            if os.path.isfile(Cave.__log_file):
                os.remove(Cave.__log_file)


def calculate(lines: list[string], part: int) -> int:
    scan = parse_paths(lines)
    cave = Cave(scan)

    return cave.produce_sand()


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
