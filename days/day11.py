import re
from collections import deque

class Part1WorryLevelReducer:
    def calculate_new_worry_level(self, item):
        return item.worry_level // 3

class Part2WorryLevelReducer:
    def __init__(self, monkeys):
        product = 1
        for monkey in monkeys:
            product *= monkey.divisor
        self.divisor = product

    def calculate_new_worry_level(self, item):
        return item.worry_level % self.divisor

class Item:
    def __init__(self, worry_level):
        self.worry_level = worry_level

    def reduce_worry_level(self, worry_level_reducer):
        self.worry_level = worry_level_reducer.calculate_new_worry_level(self)

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

    @property
    def divisor(self):
        return self.__tester.divisor

    def inspect_and_throw(self, monkeys, worry_level_reducer):
        while len(self.__items) > 0:
            item = self.__items.popleft()
            self.__inspect(item, worry_level_reducer)
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

    def __inspect(self, item, worry_level_reducer):
        self.__operation.execute(item)
        self.__inspections += 1
        item.reduce_worry_level(worry_level_reducer)

    def __calculate_monkey_to_throw_to(self, item, monkeys):
        monkey_to_throw_to = self.__tester.test(item)
        return monkeys[monkey_to_throw_to]

    def __throw(self, item, monkey_to_throw_to):
        monkey_to_throw_to.catch(item)

class Game:
    def __init__(self, rounds, worry_level_reducer):
        self.__rounds = rounds
        self.__worry_level_reducer = worry_level_reducer

    def play(self, monkeys):
        for _ in range(self.__rounds):
            for monkey in monkeys:
                monkey.inspect_and_throw(monkeys, self.__worry_level_reducer)
        return self.__get_result(monkeys)

    def __get_result(self, monkeys):
        sorted_monkeys = sorted(monkeys, key=lambda m: m.inspections, reverse=True)
        return sorted_monkeys[0].inspections * sorted_monkeys[1].inspections

def calculate(lines, part):
    monkeys = list(__parse(lines))
    match part:
        case 1:
            rounds = 20
            worry_level_reducer = Part1WorryLevelReducer()
        case 2:
            rounds = 10000
            worry_level_reducer = Part2WorryLevelReducer(monkeys)
        case _:
            raise ValueError('Invalid part')

    game = Game(rounds, worry_level_reducer)
    return game.play(monkeys)

def __parse(lines):
    start_index = 0
    while start_index < len(lines):
        yield Monkey.parse(lines, start_index)
        start_index += 7