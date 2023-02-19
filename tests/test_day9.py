from days import day9

class TestDay9:
    lines_1 = [
        "R 4",
        "U 4",
        "L 3",
        "D 1",
        "R 4",
        "D 1",
        "L 5",
        "R 2"
    ]

    lines_2 = [
        "R 5",
        "U 8",
        "L 8",
        "D 3",
        "R 17",
        "D 10",
        "L 25",
        "U 20"
    ]

    def test_day9_calculate_part1(self):
        assert day9.calculate(self.lines_1, 1) == 13

    def test_day9_calculate_part2_example1(self):
        assert day9.calculate(self.lines_1, 2) == 1

    def test_day9_calculate_part2_example2(self):
        assert day9.calculate(self.lines_2, 2) == 36