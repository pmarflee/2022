from days import day14
from days.day14 import Stuff


class TestDay14:
    lines = ['498,4 -> 498,6 -> 496,6',
             '503,4 -> 502,4 -> 502,9 -> 494,9']

    scan_result = day14.ScanResult(
        paths=[[(498, 4), (498, 6), (496, 6)],
               [(503, 4), (502, 4), (502, 9), (494, 9)]],
        min_x=494, max_x=503, max_y=9)

    def test_day14_parse_lines(self):
        assert day14.parse_paths(self.lines) == self.scan_result

    def test_day14_calculate_part1(self):
        assert day14.calculate(self.lines, 1) == 24

    def test_day14_calculate_part2(self):
        assert day14.calculate(self.lines, 2) == 93
