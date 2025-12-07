from adventofcode._2025.day6 import Day6

data = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """.splitlines()

d = Day6(data=data, debug=True)


def test_part1():
  assert d.part1() == 4277556


def test_part2():
  assert d.part2() == 3263827

