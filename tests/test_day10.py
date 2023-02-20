import os
from utils import shared
from days import day10

class TestDay10:
    
    def test_day10_calculate_part1(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        lines = shared.read_file_lines(dir_path + "\\test_day10.txt")

        assert day10.calculate(lines, 1) == 13140