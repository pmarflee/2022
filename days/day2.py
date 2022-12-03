from enum import Enum

def calculate(lines, part):
    return sum([_calculate(line) for line in lines])

def _calculate(line):
    their_choice, your_choice = _parse_line(line)
    match your_choice:
        case Shape.ROCK:
            score = 1
        case Shape.PAPER:
            score = 2
        case Shape.SCISSORS:
            score = 3
    match their_choice, your_choice:
        case (Shape.ROCK, Shape.ROCK) | (Shape.PAPER, Shape.PAPER) | (Shape.SCISSORS, Shape.SCISSORS):
            score += 3
        case (Shape.ROCK, Shape.PAPER) | (Shape.PAPER, Shape.SCISSORS) | (Shape.SCISSORS, Shape.ROCK):
            score += 6
    return score


def _parse_line(line):
    parts = line.split(' ')
    return (_parse_char(parts[0]), _parse_char(parts[1]))

def _parse_char(char):
    match char:
        case "A" | "X":
            return Shape.ROCK
        case "B" | "Y":
            return Shape.PAPER
        case "C" | "Z":
            return Shape.SCISSORS
        case _:
            raise ValueError('Invalid character')

class Shape(Enum):
    ROCK = 1,
    PAPER = 2,
    SCISSORS = 3
