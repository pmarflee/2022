from days import day3

class TestDay3:
    lines = ['vJrwpWtwJgWrhcsFMMfFFhFp',
             'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
              'PmmdzqPrVvPwwTWBwg',
              'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
              'ttgJtRGJQctTZtZT',
              'CrZsJsPPZsGzwwsLwLmpwMDw']

    def test_day3_calculate_part1(self):
        assert day3.calculate(self.lines, 1) == 157, 'incorrect value'

    def test_day3_calculate_part2(self):
        assert day3.calculate(self.lines, 2) == 70, 'incorrect value'