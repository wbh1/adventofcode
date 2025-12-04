from adventofcode._2025.day4 import Day4

data = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""".splitlines()

d = Day4(data=data)
d.debug = True

def test_part1():
    assert d.part1() == 13


def test_part2():
    assert d.part2() == 43
