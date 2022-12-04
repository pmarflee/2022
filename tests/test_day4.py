from days import day4

class TestDay4:
    lines = ['2-4,6-8',
            '2-3,4-5',
            '5-7,7-9',
            '2-8,3-7',
            '6-6,4-6',
            '2-6,4-8']

    def test_day4_calculate_part1(self):
        assert day4.calculate(self.lines, 1) == 2, 'incorrect value'

    def test_day4_calculate_part2(self):
        assert day4.calculate(self.lines, 2) == 4, 'incorrect value'
    