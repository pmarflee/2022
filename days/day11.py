import re
import time
from collections import deque

class Item:
    def __init__(self, worry_level):
        self.worry_level = worry_level

    def reduce_worry_level(self):
        self.worry_level = self.worry_level // 3

    def __repr__(self):
        return f'Item({self.worry_level=})'

class Operation:
    def __init__(self, expression):
        self.__expression = expression
        self.__code = compile(expression, "<string>", "eval")

    @property
    def expression(self):
        return self.__expression

    def execute(self, item):
        item.worry_level = eval(self.__code, {}, { "old": item.worry_level })

    def __repr__(self):
        return f'Operation({self.expression=})'

class Tester:
    def __init__(self, divisor, throw_to_when_true, throw_to_when_false):
        self.divisor = divisor
        self.throw_to_when_true = throw_to_when_true
        self.throw_to_when_false = throw_to_when_false

    def test(self, item):
        if item.worry_level % self.divisor == 0:
            return self.throw_to_when_true
        else:
            return self.throw_to_when_false

    def __repr__(self):
        return f'tester({self.divisor=}, {self.throw_to_when_true=}, {self.throw_to_when_false=})'


class Monkey:
    __regex_number = re.compile(r"^Monkey\s(\d+):$")
    __regex_tester_divisible_by = re.compile(r"\s*Test:\sdivisible\sby\s(\d+)$")
    __regex_tester_throw_to_if_true = re.compile(r"\s*If\strue:\sthrow\sto\smonkey\s(\d+)$")
    __regex_tester_throw_to_if_false = re.compile(r"\s*If\sfalse:\sthrow\sto\smonkey\s(\d+)$")

    def __init__(self, number, items, operation, tester):
        self.__number = number
        self.__items = deque(items)
        self.__operation = operation
        self.__tester = tester
        self.__inspections = 0
    
    def __repr__(self):
        return f'Monkey({self.number=})'

    @property
    def number(self):
        return self.__number

    @property
    def inspections(self):
        return self.__inspections

    def inspect_and_throw(self, monkeys, reduce_worry_levels):
        while len(self.__items) > 0:
            item = self.__items.popleft()
            self.__inspect(item, reduce_worry_levels)
            monkey_to_throw_to = self.__calculate_monkey_to_throw_to(item, monkeys)
            self.__throw(item, monkey_to_throw_to)

    def catch(self, item):
        self.__items.append(item)

    @staticmethod
    def __parse_number(line):
        match = Monkey.__regex_number.match(line)
        return int(match.group(1))
    
    @staticmethod
    def __parse_starting_items(line):
        split_line = line.split(':')
        return [Item(int(n)) for n in split_line[1].split(',')]

    @staticmethod
    def __parse_operation(line):
        split_line = line.split("=")
        return Operation(split_line[1].strip())

    @staticmethod
    def __parse_tester(lines, start_index):
        match_divisble_by = Monkey.__regex_tester_divisible_by.match(lines[start_index])
        match_throw_to_if_true = Monkey.__regex_tester_throw_to_if_true.match(lines[start_index + 1])
        match_throw_to_if_false = Monkey.__regex_tester_throw_to_if_false.match(lines[start_index + 2])
        return Tester(
            int(match_divisble_by.group(1)), 
            int(match_throw_to_if_true.group(1)),
            int(match_throw_to_if_false.group(1)))

    @staticmethod
    def parse(lines, start_index):
        number = Monkey.__parse_number(lines[start_index])
        items = Monkey.__parse_starting_items(lines[start_index + 1])
        operation = Monkey.__parse_operation(lines[start_index + 2])
        tester = Monkey.__parse_tester(lines, start_index + 3)
        return Monkey(number, items, operation, tester)

    def __inspect(self, item, reduce_worry_levels):
        self.__operation.execute(item)
        self.__inspections += 1
        if reduce_worry_levels:
            item.reduce_worry_level()

    def __calculate_monkey_to_throw_to(self, item, monkeys):
        monkey_to_throw_to = self.__tester.test(item)
        return monkeys[monkey_to_throw_to]

    def __throw(self, item, monkey_to_throw_to):
        monkey_to_throw_to.catch(item)

class Game:
    def __init__(self, rounds, reduce_worry_levels):
        self.__rounds = rounds
        self.__reduce_worry_levels = reduce_worry_levels

    def play(self, monkeys):
        for round in range(self.__rounds):
            print(f"Round: {round}")
            for monkey in monkeys:
                monkey.inspect_and_throw(monkeys, self.__reduce_worry_levels)
        return self.__get_result(monkeys)

    def __get_result(self, monkeys):
        sorted_monkeys = sorted(monkeys, key=lambda m: m.inspections, reverse=True)
        return sorted_monkeys[0].inspections * sorted_monkeys[1].inspections

def calculate(lines, part):
    match part:
        case 1:
            rounds = 20
            reduce_worry_levels = True
        case 2:
            rounds = 10000
            reduce_worry_levels = False
        case _:
            raise ValueError('Invalid part')

    monkeys = list(__parse(lines))
    game = Game(rounds, reduce_worry_levels)
    return game.play(monkeys)

def __parse(lines):
    start_index = 0
    while start_index < len(lines):
        yield Monkey.parse(lines, start_index)
        start_index += 7