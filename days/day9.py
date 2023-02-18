from __future__ import annotations
from typing import List
from enum import IntEnum

def calculate(lines: List[str], part: int):
    rope = Rope()
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

class Position:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __eq__(self, other: Position):
        if not isinstance(other, Position):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def add(self, x: int, y: int) -> Position:
        return Position(self.x + x, self.y + y)

class Rope:
    def __init__(self) -> None:
        self.head = Position()
        self.tail = Position()
        self.visited = set([self.tail])

    def move(self, instruction: Instruction):
        for _ in range(instruction.distance):
            self.__move_head(instruction)
            self.__move_tail()

    def __move_head(self, instruction: Instruction) -> None:
        match instruction.direction:
            case Direction.UP:
                self.head = Position(self.head.x, self.head.y + 1)
            case Direction.DOWN:
                self.head = Position(self.head.x, self.head.y - 1)
            case Direction.LEFT:
                self.head = Position(self.head.x - 1, self.head.y)
            case Direction.RIGHT:
                self.head = Position(self.head.x + 1, self.head.y)

    def __move_tail(self) -> None:
        offset_x, offset_y = self.__get_head_tail_offset()
        if offset_x > 1:
            change_x = 1
            change_y = offset_y
        elif offset_x < -1:
            change_x = -1
            change_y = offset_y
        elif offset_y > 1:
            change_x = offset_x
            change_y = 1
        elif offset_y < -1:
            change_x = offset_x
            change_y = -1
        else:
            change_x = 0
            change_y = 0

        if change_x != 0 or change_y != 0:
            self.tail = self.tail.add(change_x, change_y)
            self.visited.add(self.tail)

    def __get_head_tail_offset(self) -> tuple[int, int]:
        return (self.head.x - self.tail.x, self.head.y - self.tail.y)
