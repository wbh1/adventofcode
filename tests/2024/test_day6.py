from adventofcode._2024.day6 import Day6

data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".splitlines()

d = Day6(data=data)


def test_part1():
  assert d.part1() == 41


def test_part2():
  assert d.part2() == 6

