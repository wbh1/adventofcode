from adventofcode._2024.day2 import Day2

data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".splitlines()

d = Day2(data=data)


def test_part1():
    assert d.part1() == 2


def test_part2():
    assert d.part2() == 4
