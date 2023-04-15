from days import day14

class TestDay14:
    lines = ['498,4 -> 498,6 -> 496,6',
             '503,4 -> 502,4 -> 502,9 -> 494,9']
    
    parse_expected = [ [ (498,4), (498,6), (496,6 ) ],
                       [ (503,4), (502,4), (502,9), (494,9 ) ] ]
    
    def test_day14_parse_lines(self):
        assert day14.parse_lines(self.lines) == self.parse_expected