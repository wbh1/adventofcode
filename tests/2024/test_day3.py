from adventofcode._2024.day3 import Day3


def test_part1():
    data = r"xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))".splitlines()
    d = Day3(data=data)
    assert d.part1() == 161


def test_part2():
    data = r"xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))".splitlines()
    d = Day3(data=data)
    assert d.part2() == 48

