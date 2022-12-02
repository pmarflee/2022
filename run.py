import time
from utils import shared
from days import day1

def run(action, day, part, path):
    start = time.time()
    result = action(path)
    end = time.time()

    print(f"Day {day}, Part {part}: {result} ({end - start}s)")

print("Advent of Code 2022")
print("===================")

# Day 1

run(lambda path: day1.calculate(shared.read_file_lines(path), 1), 1, 1, 'data\\day1.txt')