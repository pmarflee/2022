from abc import ABC, abstractmethod

class Register:
    def __init__(self, value= 1):
        self.__value = value

    @property
    def value(self):
        return self.__value

    def increment(self, value):
        self.__value += value

class Instruction(ABC):
    def __init__(self, cycles):
        self.__cycles = cycles

    @property
    def cycles(self):
        return self.__cycles

class Noop(Instruction):
    def __init__(self):
        super().__init__(1)

    def update(self, register):
        pass

class AddX(Instruction):
    def __init__(self, value):
        super().__init__(2)
        self.value = value

    def update(self, register):
        register.increment(self.value)

class ClockCircuit:
    def __init__(self) -> None:
        self.__cycles = 0
    
    @property
    def cycles(self):
        return self.__cycles

    def tick(self, action) -> None:
        self.__cycles += 1
        action(self.__cycles)

class Device(ABC):
    def __init__(self) -> None:
        self.__x = Register()
        self.__clock = ClockCircuit()

    @property
    def X(self):
        return self.__x.value

    @property
    def clock(self):
        return self.__clock

    @property
    def cycles(self) -> int:
        return self.clock.cycles
    
    @abstractmethod
    def clock_ticked(self, cycles):
        pass
    
    def execute(self, instruction):
        for _ in range(instruction.cycles):
            self.clock.tick(self.clock_ticked)
        instruction.update(self.__x)

class CPU(Device):
    __sample_cycles = [20, 60, 100, 140, 180, 220]

    def __init__(self):
        super().__init__()
        self.__signal_strengths = []

    @property
    def sum_signal_strengths(self):
        return sum(self.__signal_strengths)

    def clock_ticked(self, cycles):
        if cycles in CPU.__sample_cycles:
            self.__signal_strengths.append(cycles * self.X)

def calculate(lines, part):
    cpu = CPU()
    for line in lines:
        instruction = __parse(line)
        cpu.execute(instruction)
    return cpu.sum_signal_strengths

def __parse(line):
    if line == 'noop':
        return Noop()
    parts = line.split(' ')
    return AddX(int(parts[1]))