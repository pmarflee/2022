import time
from utils import shared
from days import day1, day2

def run(action, day, part, path):
    start = time.time()
    result = action(path)
    end = time.time()

    print(f"Day {day}, Part {part}: {result} ({end - start}s)")

print("Advent of Code 2022")
print("===================")

# Day 1

run(lambda path: day1.calculate(shared.read_file_lines(path), 1), 1, 1, 'data\\day1.txt')
run(lambda path: day1.calculate(shared.read_file_lines(path), 2), 1, 2, 'data\\day1.txt')

# Day 2

run(lambda path: day2.calculate(shared.read_file_lines(path), 1), 2, 1, 'data\\day2.txt')