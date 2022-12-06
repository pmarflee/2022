from days import day5

class TestDay5:
    lines = ['    [D]    ',
             '[N] [C]    ',
             '[Z] [M] [P]',
             '1   2   3 ',
             '',
             'move 1 from 2 to 1',
             'move 3 from 1 to 3',
             'move 2 from 2 to 1',
             'move 1 from 1 to 2']

    def test_day5_parse_input_stacks(self):
        ship = day5.parse_input(self.lines)
        assert ship.stacks[0] == ['Z','N']
        assert ship.stacks[1] == ['M','C','D']
        assert ship.stacks[2] == ['P']

    def test_day5_parse_input_instructions(self):
        ship = day5.parse_input(self.lines)
        assert ship.instructions[0] == day5.Instruction(1, 2, 1)
        assert ship.instructions[1] == day5.Instruction(3, 1, 3)
        assert ship.instructions[2] == day5.Instruction(2, 2, 1)
        assert ship.instructions[3] == day5.Instruction(1, 1, 2)

    def test_day5_calculate_part1(self):
        assert day5.calculate(self.lines, 1) == 'CMZ', 'incorrect value'