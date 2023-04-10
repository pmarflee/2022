from days import day12

class TestDay12:
    lines = [ 'Sabqponm',
              'abcryxxl',
              'accszExk',
              'acctuvwj',
              'abdefghi' ]

    def test_day12_parse(self):
        elevations = day12.create_elevations()
        expected = [ [ ('S', 1), ('a', 1), ('b', 2), ('q', 17), ('p', 16), ('o', 15), ('n', 14), ('m', 13) ],
                     [ ('a', 1), ('b', 2), ('c', 3), ('r', 18), ('y', 25), ('x', 24), ('x', 24), ('l', 12) ],
                     [ ('a', 1), ('c', 3), ('c', 3), ('s', 19), ('z', 26), ('E', 26), ('x', 24), ('k', 11) ],
                     [ ('a', 1), ('c', 3), ('c', 3), ('t', 20), ('u', 21), ('v', 22), ('w', 23), ('j', 10) ],
                     [ ('a', 1), ('b', 2), ('d', 4), ('e', 5), ('f', 6), ('g', 7), ('h', 8), ('i', 9) ] ]
        
        assert day12.parse(self.lines, elevations) == expected

    def test_day12_calculate_part1(self):
        assert day12.calculate(self.lines, 1) == 31

    def test_day12_calculate_part2(self):
        assert day12.calculate(self.lines, 2) == 29