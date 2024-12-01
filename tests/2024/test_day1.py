from adventofcode._2024.day1 import Day1

data = """3   4
4   3
2   5
1   3
3   9
3   3""".splitlines()

d = Day1(data=data)


def test_part1():
    assert d.part1() == 11


def test_part2():
    assert d.part2() == 31
