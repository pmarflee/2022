import time
from utils import shared
from days import day1, day2, day3, day4, day5, day6, day7, day8, day9, day10, day11, day12

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

# Day 6

run(lambda path: day6.calculate(shared.read_file_content(path), 1), 6, 1, 'data\\day6.txt')
run(lambda path: day6.calculate(shared.read_file_content(path), 2), 6, 2, 'data\\day6.txt')

# Day 7

run(lambda path: day7.calculate(shared.read_file_lines(path), 1), 7, 1, 'data\\day7.txt')
run(lambda path: day7.calculate(shared.read_file_lines(path), 2), 7, 2, 'data\\day7.txt')

# Day 8

run(lambda path: day8.calculate(shared.read_file_lines(path), 1), 8, 1, 'data\\day8.txt')
run(lambda path: day8.calculate(shared.read_file_lines(path), 2), 8, 2, 'data\\day8.txt')

# Day 9

run(lambda path: day9.calculate(shared.read_file_lines(path), 1), 9, 1, 'data\\day9.txt')
run(lambda path: day9.calculate(shared.read_file_lines(path), 2), 9, 2, 'data\\day9.txt')

# Day 10

run(lambda path: day10.calculate(shared.read_file_lines(path), 1), 10, 1, 'data\\day10.txt')
run(lambda path: day10.calculate(shared.read_file_lines(path), 2), 10, 2, 'data\\day10.txt')

# Day 11

run(lambda path: day11.calculate(shared.read_file_lines(path), 1), 11, 1, 'data\\day11.txt')
run(lambda path: day11.calculate(shared.read_file_lines(path), 2), 11, 2, 'data\\day11.txt')

# Day 12

run(lambda path: day12.calculate(shared.read_file_lines(path), 1), 12, 1, 'data\\day12.txt')

print()
print(f"Total elapsed: {total_elapsed}s")