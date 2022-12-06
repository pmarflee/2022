import time
from utils import shared
from days import day1, day2, day3, day4, day5

total_elapsed = 0.0

def run(action, day, part, path):
    global total_elapsed

    start = time.time()
    result = action(path)
    end = time.time()

    elapsed = end - start
    total_elapsed += elapsed

    print(f"Day {day}, Part {part}: {result} ({elapsed}s)")

print("Advent of Code 2022")
print("===================")
print()

# Day 1

run(lambda path: day1.calculate(shared.read_file_lines(path), 1), 1, 1, 'data\\day1.txt')
run(lambda path: day1.calculate(shared.read_file_lines(path), 2), 1, 2, 'data\\day1.txt')

# Day 2

run(lambda path: day2.calculate(shared.read_file_lines(path), 1), 2, 1, 'data\\day2.txt')
run(lambda path: day2.calculate(shared.read_file_lines(path), 2), 2, 2, 'data\\day2.txt')

# Day 3

run(lambda path: day3.calculate(shared.read_file_lines(path), 1), 3, 1, 'data\\day3.txt')
run(lambda path: day3.calculate(shared.read_file_lines(path), 2), 3, 2, 'data\\day3.txt')

# Day 4

run(lambda path: day4.calculate(shared.read_file_lines(path), 1), 4, 1, 'data\\day4.txt')
run(lambda path: day4.calculate(shared.read_file_lines(path), 2), 4, 2, 'data\\day4.txt')

# Day 5

run(lambda path: day5.calculate(shared.read_file_lines(path), 1), 5, 1, 'data\\day5.txt')
run(lambda path: day5.calculate(shared.read_file_lines(path), 2), 5, 2, 'data\\day5.txt')

print()
print(f"Total elapsed: {total_elapsed}s")