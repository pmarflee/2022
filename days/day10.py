from typing import List
from abc import ABC, abstractmethod

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

class ClockCircuit:
    def __init__(self) -> None:
        self.cycles = 0
    
    def tick(self) -> None:
        self.cycles += 1

class CPU:
    sample_cycles = [20, 60, 100, 140, 180, 220]

    def __init__(self, clock_circuit: ClockCircuit) -> None:
        self.X = 1
        self.__clock_circuit = clock_circuit
        self.__signal_strengths = []

    @property
    def sum_signal_strengths(self):
        return sum(self.__signal_strengths)

    def execute(self, instruction: Instruction):
        for _ in range(instruction.cycles):
            self.__clock_circuit.tick()
            if self.__clock_circuit.cycles in CPU.sample_cycles:
                self.__signal_strengths.append(self.__clock_circuit.cycles * self.X)
        if isinstance(instruction, AddX):
            self.X += instruction.value

def calculate(lines: List[str], part: int):
    cpu = CPU(ClockCircuit())
    for line in lines:
        instruction = __parse(line)
        cpu.execute(instruction)
    return cpu.sum_signal_strengths

def __parse(line: str) -> Instruction:
    if line == 'noop':
        return Noop()
    parts = line.split(' ')
    return AddX(int(parts[1]))