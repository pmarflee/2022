from days import day1

class TestDay1:
    lines = ['1000',
             '2000',
             '3000',
             '',
             '4000',
             '',
             '5000',
             '6000',
             '',
             '7000',
             '8000',
             '9000',
             '',
             '10000']
    def test_day1_calculate_part1(self):
        assert day1.calculate(self.lines, 1) == 24000, 'incorrect value'

    def test_day1_calculate_part2(self):
        assert day1.calculate(self.lines, 2) == 45000, 'incorrect value'