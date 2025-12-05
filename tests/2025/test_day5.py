from adventofcode._2025.day5 import Day5

data = """3-5
10-14
16-20
12-18

1
5
8
11
17
32""".splitlines()

d = Day5(data=data)
d.debug = True


def test_part1():
  assert d.part1() == 3


def test_part2():
  assert d.part2() == 14


def test_alt_input():
  d.ingredient_ranges = """3-5
10-14
16-20
12-18
13-14
13-13""".splitlines()

  assert d.part2() == 14
  assert d.ingredient_ranges == ["3-5", "10-20"]


def test_sorting():
  d.ingredient_ranges = """464049531839818-471121630979966
465692950220528-471121630979966
475335800364972-475864701844976
475864701844976-476402660690655
478308149137049-478863092682069
478863092682069-479234503506978""".splitlines()

  d.flatten_ranges()
  assert d.ingredient_ranges == [
    "464049531839818-471121630979966",
    "475335800364972-476402660690655",
    "478308149137049-479234503506978",
  ]
