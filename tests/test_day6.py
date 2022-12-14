import pytest
from days import day6

pytestmark = pytest.mark.parametrize("buffer, expected_part_1, expected_part_2", [
    ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7, 19),
    ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5, 23),
    ('nppdvjthqldpwncqszvftbrmjlhg', 6, 23),
    ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10, 29),
    ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11, 26)])

class TestDay6:
    def test_day6_calculate_part1(self, buffer, expected_part_1, expected_part_2):
        assert day6.calculate(buffer, 1) == expected_part_1

    def test_day6_calculate_part2(self, buffer, expected_part_1, expected_part_2):
        assert day6.calculate(buffer, 2) == expected_part_2