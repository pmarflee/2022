import pytest
from days import day6

pytestmark = pytest.mark.parametrize("buffer, expected", [
    ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7),
    ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5),
    ('nppdvjthqldpwncqszvftbrmjlhg', 6),
    ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10),
    ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11)])

class TestDay6:
    def test_day6_calculate_part1(self, buffer, expected):
        assert day6.calculate(buffer, 1) == expected