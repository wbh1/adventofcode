from adventofcode._2025.day1 import Day1
import pytest

data = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""".splitlines()

d = Day1(data=data)


def test_part1():
    assert d.part1() == 3


def test_part2():
    d.pos = 50
    d.zero_passes = 0
    d.part1()
    assert d.part2() == 6

@pytest.mark.parametrize(["pos", "movement", "expected"], [(0, 690, 6), (90, 392, 4), (82, 18, 1)])
def test_right_wrap(pos, movement, expected):
    d.pos = pos
    d.zero_passes = 0
    d.move(movement)
    assert d.zero_passes == expected

@pytest.mark.parametrize(["pos", "movement", "expected"], [(71, -871, 9), (0, -17, 0), (55, -55, 1)])
def test_left_wrap(pos, movement, expected):
    d.pos = pos
    d.zero_passes = 0
    d.move(movement)
    assert d.zero_passes == expected
