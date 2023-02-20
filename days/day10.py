from typing import List
from abc import ABC, abstractmethod

def calculate(lines: List[str], part: int):
    cpu = CPU()
    for line in lines:
        cpu.execute(line)
    return cpu.sum_signal_strengths

class Instruction:
    def __init__(self, cycles):
        self.cycles = cycles

class Noop(Instruction):
    def __init__(self):
        super().__init__(1)

class AddX(Instruction):
    def __init__(self, value: int):
        super().__init__(2)
        self.value = value

class CPU:
    sample_cycles = [20, 60, 100, 140, 180, 220]

    def __init__(self):
        self.X = 1
        self.__cycles = 0
        self.__signal_strengths = []

    @property
    def sum_signal_strengths(self):
        return sum(self.__signal_strengths)

    def execute(self, line: str):
        instruction = CPU.__parse_instruction(line)
        for _ in range(instruction.cycles):
            self.__cycles += 1
            if self.__cycles in CPU.sample_cycles:
                self.__signal_strengths.append(self.__cycles * self.X)
        if isinstance(instruction, AddX):
            self.X += instruction.value

    @staticmethod
    def __parse_instruction(line: str) -> Instruction:
        if line == 'noop':
            return Noop()
        parts = line.split(' ')
        return AddX(int(parts[1]))

