from adventofcode._2025.day3 import Day3
import pytest

data = """987654321111111
811111111111119
234234234234278
818181911112111""".splitlines()

d = Day3(data=data)
d.debug = True

@pytest.mark.parametrize(["bank", "joltage"], [(data[0], 98), (data[1], 89), (data[2], 78), (data[3], 92)])
def test_joltage_part1(bank, joltage):
    assert d.max_joltage_part1(bank) == joltage

@pytest.mark.parametrize(["bank", "joltage"], [(data[0], 987654321111), (data[1], 811111111119), (data[2], 434234234278), (data[3], 888911112111)])
def test_joltage_part2(bank, joltage):
    assert d.max_joltage_part2(bank) == joltage

def test_part1():
    assert d.part1() == 357


def test_part2():
    assert d.part2() == 3121910778619
