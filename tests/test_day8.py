from days import day8

class TestDay8:
    lines = [ "30373", "25512", "65332", "33549", "35390" ]

    def test_day8_calculate_part1(self):
        assert day8.calculate(self.lines, 1) == 21

    def test_day8_calculate_part2(self):
        pass