from days import day13

class TestDay13:
    lines = [ '[1,1,3,1,1]',
              '[1,1,5,1,1]',
              '',
              '[[1],[2,3,4]]',
              '[[1],4]',
              '',
              '[9]',
              '[[8,7,6]]',
              '',
              '[[4,4],4,4]',
              '[[4,4],4,4,4]',
              '',
              '[7,7,7,7]',
              '[7,7,7]',
              '',
              '[]',
              '[3]',
              '',
              '[[[]]]',
              '[[]]',
              '',
              '[1,[2,[3,[4,[5,6,7]]]],8,9]',
              '[1,[2,[3,[4,[5,6,0]]]],8,9]']

    def test_day13_calculate_part1(self):
        assert day13.calculate(self.lines, 1) == 13

    def test_day13_calculate_part2(self):
        assert day13.calculate(self.lines, 2) == 140