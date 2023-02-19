from __future__ import annotations
from typing import List
from enum import IntEnum
from utils import shared

def calculate(lines: List[str], part: int):
    length = 2 if part == 1 else 10
    rope = Rope(length)
    for line in lines:
        instruction = _parse(line)
        rope.move(instruction)
    return len(rope.visited)

def _parse(line: str):
    direction = _parse_direction(line)
    distance = _parse_distance(line)
    
    return Instruction(direction, distance)

def _parse_direction(line: str):
    match line[0]:
        case 'U':
            return Direction.UP
        case 'D':
            return Direction.DOWN
        case 'L':
            return Direction.LEFT
        case 'R':
            return Direction.RIGHT

def _parse_distance(line: str):
    return int(line[2:])

class Direction(IntEnum):
    UP = 1,
    DOWN = 2,
    LEFT = 3,
    RIGHT = 4

class Instruction:
    def __init__(self, direction: Direction, distance: int) -> None:
       self.direction = direction
       self.distance = distance

class Knot:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Knot({self.x=}, {self.y=})'

    @property
    def position(self) -> tuple[int, int]:
        return (self.x, self.y)

    def add(self, x: int, y: int) -> Knot:
        return Knot(self.x + x, self.y + y)

    def get_position_relative_to(self, other: Knot) -> tuple[int, int, bool]:
        offset_x, offset_y = self.x - other.x, self.y - other.y
        return (offset_x, offset_y, abs(offset_x) <= 1 and abs(offset_y) <= 1)

class Rope:
    def __init__(self, length: int) -> None:
        self.knots = list(Knot() for _ in range(length))
        self.visited = set([self.tail.position])

    @property
    def head(self):
        return self.knots[0]

    @head.setter
    def head(self, value: Knot):
        self.knots[0] = value

    @property
    def tail(self):
        return self.knots[len(self.knots) - 1]

    def move(self, instruction: Instruction):
        for _ in range(instruction.distance):
            self.__move_head(instruction)
            for i in range(1, len(self.knots)):
                self.__move_knot(i, self.knots[i], self.knots[i - 1])

    def __move_head(self, instruction: Instruction) -> None:
        match instruction.direction:
            case Direction.UP:
                self.head = self.head.add(0, 1)
            case Direction.DOWN:
                self.head = self.head.add(0, -1)
            case Direction.LEFT:
                self.head = self.head.add(-1, 0)
            case Direction.RIGHT:
                self.head = self.head.add(1, 0)

    def __move_knot(self, knot_index: int, knot: Knot, knot_previous: Knot) -> None:
        offset_x, offset_y, is_touching = knot_previous.get_position_relative_to(knot)

        if not is_touching:
            change_x, change_y = shared.sign(offset_x), shared.sign(offset_y)
            knot_new = knot.add(change_x, change_y)
            new_position = knot_new.position
            if knot == self.tail:
                self.visited.add(new_position)
            self.knots[knot_index] = knot_new