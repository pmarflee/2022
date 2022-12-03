from days import day3

class TestDay3:
    lines = ['vJrwpWtwJgWrhcsFMMfFFhFp',
             'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
              'PmmdzqPrVvPwwTWBwg',
              'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
              'ttgJtRGJQctTZtZT',
              'CrZsJsPPZsGzwwsLwLmpwMDw']

    def test_day2_calculate_part1(self):
        assert day3.calculate(self.lines, 1) == 157, 'incorrect value'