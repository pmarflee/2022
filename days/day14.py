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

        cave.set_stuff(Stuff.SAND, *cave.source)

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

        self.cave.log_grain_location()

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

                    if stuff is None or stuff == Stuff.SOURCE:
                        self.cave.move_sand(self.location, (next_x, next_y))
                        self.__location = (next_x, next_y)
                        new_result = MoveResult.FALLING
                        self.cave.log_grain_location()
                        break

            result = new_result if new_result is not None else MoveResult.RESTED

    def __can_move_x(self, x_offset: int) -> bool:
        return self.cave.get_stuff(self.location[0] + x_offset, self.location[1]) is None

    def __check_next_location(self, x_offset: int, y_offset: int) -> Optional[tuple[int, int, Optional[Stuff]]]:
        if self.location is None:
            raise TypeError

        location_x, location_y = self.location
        next_x, next_y = location_x + x_offset, location_y + y_offset

        if next_y > self.cave.height:
            return None

        if next_x > self.cave.max_x or next_x < self.cave.min_x:
            return next_x, next_y, Stuff.ROCK if self.cave.has_floor and next_y == self.cave.height else None

        return next_x, next_y, self.cave.get_stuff(next_x, next_y)


class Cave:
    __log_file = 'day14.txt'

    def __init__(self, scan: ScanResult, has_floor: bool):
        self.__offset = scan.min_x
        self.__source = (500, 0)
        self.__height = scan.max_y + (2 if has_floor else 0)
        self.__min_x = scan.min_x
        self.__max_x = scan.max_x
        self.__has_floor = has_floor
        self.__current_grain = None
        self.__last_grain = None

        self.__data: dict[int, list[Optional[Stuff]]] = dict(
            [(i, self.__create_column()) for i in range(scan.min_x, scan.max_x + 1)])

        for line in scan.paths:
            for (x_previous, y_previous), (x_current, y_current) in pairwise(line):
                for x, y in Cave.__get_rock_range(x_previous, y_previous, x_current, y_current):
                    self.set_stuff(Stuff.ROCK, x, y)

    @property
    def data(self):
        return self.__data

    @property
    def source(self):
        return self.__source

    @property
    def min_x(self):
        return self.__min_x

    @property
    def max_x(self):
        return self.__max_x

    @property
    def height(self):
        return self.__height

    @property
    def has_floor(self):
        return self.__has_floor

    @property
    def current_grain(self) -> Optional[Grain]:
        return self.__current_grain

    @property
    def last_grain(self) -> Optional[Grain]:
        return self.__last_grain

    def produce_sand(self) -> int:
        count = 0
        i = 0

        self.__clear_log()
        Cave.__log_count(i)
        self.__log_cave()

        while True:
            i += 1
            self.__current_grain = grain = Grain(self)
            Cave.__log_count(i)
            grain.drop()
            if grain.is_lost:
                break
            else:
                self.__last_grain = grain
                self.__log_cave()

                count += 1

                if self.is_full:
                    self.__log_cave()
                    break

        return count

    def move_sand(self, from_location: tuple[int, int], to_location: tuple[int, int]):
        self.set_stuff(None, *from_location)
        self.set_stuff(Stuff.SAND, *to_location)

    def set_stuff(self, stuff: Optional[Stuff], x: int, y: int):
        if x not in self.data:
            self.data[x] = self.__create_column()

            if x < self.min_x:
                self.__min_x = x
            elif x > self.max_x:
                self.__max_x = x

        self.data[x][y] = stuff

    def get_stuff(self, x: int, y: int) -> Optional[Stuff]:
        return self.data[x][y]

    @property
    def is_full(self):
        return self.get_stuff(*self.source) == Stuff.SAND

    @staticmethod
    def __get_rock_range(x_previous: int, y_previous: int, x_current: int, y_current: int) -> list[
        tuple[int, int]]:
        if x_previous == x_current:
            min_y, max_y = min(y_previous, y_current), max(y_previous, y_current)
            return [(x_previous, y) for y in range(min_y, max_y + 1)]
        else:
            min_x, max_x = min(x_previous, x_current), max(x_previous, x_current)
            return [(x, y_previous) for x in range(min_x, max_x + 1)]

    def __create_column(self):
        return [Stuff.ROCK if self.has_floor and i == self.height else None for i in range(self.height + 1)]

    @staticmethod
    def __log_count(count: int):
        if enable_logging:
            with open(Cave.__log_file, 'a') as log_file:
                log_file.write(f"{count}\n")

    def __log_cave(self, log: bool = False):
        if enable_logging or log:
            with open(Cave.__log_file, 'a') as log_file:
                log_file.writelines(f"{self}\n")

    def log_grain_location(self) -> None:
        if enable_logging:
            with open(Cave.__log_file, 'a') as log_file:
                log_file.write(f"Grain location: {self.current_grain.location}\n")

    @staticmethod
    def __clear_log():
        if enable_logging:
            if os.path.isfile(Cave.__log_file):
                os.remove(Cave.__log_file)

    def __str__(self):
        result = '\r\n'

        keys = list(self.data.keys())
        min_x, max_x = min(keys), max(keys)

        for row in range(self.__height + 1):
            for col in range(min_x, max_x + 1):
                match self.data[col][row]:
                    case Stuff.ROCK:
                        c = '#'
                    case Stuff.SAND:
                        c = 'O' if self.last_grain is not None and (col, row) == self.last_grain.location else 'o'
                    case Stuff.SOURCE:
                        c = '+'
                    case _:
                        c = '+' if (col, row) == self.source else '.'

                result += c

            result += '\n'

        return result


def calculate(lines: list[string], part: int) -> int:
    scan = parse_paths(lines)
    cave = Cave(scan, part == 2)

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
