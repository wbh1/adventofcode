from adventofcode._2024.day5 import Day5

data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

d = Day5(data=data)


def test_part1():
    print("rules", d.rules)
    print("pages", d.page_runs)
    assert d.part1() == 143


def test_part2():
    assert d.part2() == 123


def test_bubble_sort():
    assert d.bubble_sort(["97", "13", "75", "29", "47"]) == [
        "97",
        "75",
        "47",
        "29",
        "13",
    ]
