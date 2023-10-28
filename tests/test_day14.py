from days import day14
from days.day14 import Stuff


class TestDay14:
    lines = ['498,4 -> 498,6 -> 496,6',
             '503,4 -> 502,4 -> 502,9 -> 494,9']

    scan_result = day14.ScanResult(
        paths=[[(498, 4), (498, 6), (496, 6)],
         [(503, 4), (502, 4), (502, 9), (494, 9)]],
        min_x=494, max_x=503, max_y=9)

    cave_data = [
        [None, None, None, None, None, None, Stuff.SOURCE, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, Stuff.ROCK, None, None, None, Stuff.ROCK, Stuff.ROCK],
        [None, None, None, None, Stuff.ROCK, None, None, None, Stuff.ROCK, None],
        [None, None, Stuff.ROCK, Stuff.ROCK, Stuff.ROCK, None, None, None, Stuff.ROCK, None],
        [None, None, None, None, None, None, None, None, Stuff.ROCK, None],
        [None, None, None, None, None, None, None, None, Stuff.ROCK, None],
        [Stuff.ROCK, Stuff.ROCK, Stuff.ROCK, Stuff.ROCK, Stuff.ROCK, Stuff.ROCK, Stuff.ROCK, Stuff.ROCK, Stuff.ROCK, None]
    ]

    def test_day14_parse_lines(self):
        assert day14.parse_paths(self.lines) == self.scan_result

    def test_day14_draw_cave(self):
        assert day14.Cave(self.scan_result).data == self.cave_data