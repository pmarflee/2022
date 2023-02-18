import pytest

from days import day9

class TestDay9:
    lines = [
        "R 4",
        "U 4",
        "L 3",
        "D 1",
        "R 4",
        "D 1",
        "L 5",
        "R 2"
    ]

    def test_day9_calculate_part1(self):
        assert day9.calculate(self.lines, 1) == 13

    @pytest.mark.skip()
    def test_day9_calculate_part2(self):
        pass