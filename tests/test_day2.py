from days import day2

class TestDay2:
    lines = ['A Y', 'B X', 'C Z']

    def test_day2_calculate_part1(self):
        assert day2.calculate(self.lines, 1) == 15, 'incorrect value'

    def test_day2_calculate_part2(self):
        assert day2.calculate(self.lines, 2) == 12, 'incorrect value'
