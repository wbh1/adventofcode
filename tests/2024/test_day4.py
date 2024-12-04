from adventofcode._2024.day4 import Day4

data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".splitlines()

d = Day4(data=data)


def test_part1():
    assert d.part1() == 18


def test_part2():
    assert d.part2() == 9
