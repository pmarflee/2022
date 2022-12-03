from enum import Enum

def calculate(lines, part):
    return sum([_calculate(line, part) for line in lines])

def _calculate(line, part):
    their_choice, your_choice = _parse_line(line, part)
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


def _parse_line(line, part):
    parts = line.split(' ')
    their_choice = _parse_char(parts[0])
    match part:
        case 1:
            your_choice = _parse_char(parts[1])
        case 2:
            your_choice = _parse_char_part2(parts[1], their_choice)
        case _:
            raise ValueError('Invalid part')
    return (their_choice, your_choice)

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

def _parse_char_part2(char, their_choice):
    match char, their_choice:
        case "X", Shape.ROCK:
            return Shape.SCISSORS
        case "X", Shape.PAPER:
            return Shape.ROCK
        case "X", Shape.SCISSORS:
            return Shape.PAPER
        case "Y", Shape.ROCK:
            return Shape.ROCK
        case "Y", Shape.PAPER:
            return Shape.PAPER
        case "Y", Shape.SCISSORS:
            return Shape.SCISSORS
        case "Z", Shape.ROCK:
            return Shape.PAPER
        case "Z", Shape.PAPER:
            return Shape.SCISSORS
        case "Z", Shape.SCISSORS:
            return Shape.ROCK
        case _:
            raise ValueError('Invalid values')

class Shape(Enum):
    ROCK = 1,
    PAPER = 2,
    SCISSORS = 3
