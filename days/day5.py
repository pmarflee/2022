import re

def calculate(lines, part):
    ship = parse_input(lines, part)
    return ship.execute_instructions()

def parse_input(lines, part):
    crate_lines = []
    instructions = []
    for line in lines:
        if (crate_line := _parse_crates(line)):
            crate_lines.append(crate_line)
        elif (parsed_instruction := _parse_instruction(line)):
            instructions.append(parsed_instruction)
        elif (parsed_stacks := _parse_stacks(line)):
            count_stacks = parsed_stacks
    return Ship(part, crate_lines, count_stacks, instructions)

def _parse_crates(line):
    if line.find('[') > -1 and line.find(']') > -1:
        return [line[n+1] for n in range(0, len(line), 4)]

def _parse_stacks(line):
    if (parsed := _regex_stacks.findall(line)) != []:
        return max([int(n) for n in parsed])

def _parse_instruction(line):
    if (parsed := _regex_instruction.match(line)):
        return Instruction(int(parsed.group(1)), int(parsed.group(2)), int(parsed.group(3)))

class Ship:
    def __init__(self, part, crate_lines, count_stacks, instructions):
        self.part = part
        self.stacks = [[] for _ in range(count_stacks)]
        for line in reversed(crate_lines):
            for n in range(count_stacks):
                crate = line[n]
                if crate != ' ':
                    self.stacks[n].append(crate)
        self.instructions = instructions
                    
    def execute_instructions(self):
        for instruction in self.instructions:
            source_index = instruction.source - 1 
            target_index = instruction.target - 1
            source = self.stacks[source_index]
            target = self.stacks[target_index]
            match self.part:
                case 1:
                    for _ in range(instruction.number):
                        crate = source.pop()
                        target.append(crate)
                case 2:
                    left, taken = source[:len(source) - instruction.number], source[-instruction.number:]
                    self.stacks[source_index] = left
                    target.extend(taken)
        return ''.join([stack[len(stack) - 1] for stack in self.stacks])

class Instruction:
    def __init__(self, number, source, target):
        self.number = number
        self.source = source
        self.target = target

    def __eq__(self, other):
        if not isinstance(other, Instruction):
            return NotImplemented
        return self.number == other.number and self.source == other.source and self.target == other.target

_regex_stacks = re.compile(r"\b(\d)\b")
_regex_instruction = re.compile(r"^move\s(\d+)\sfrom\s(\d)\sto\s(\d)$")