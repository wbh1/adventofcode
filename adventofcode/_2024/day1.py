from collections import Counter
from typing import List

from adventofcode.utils.Puzzle import Puzzle


class Day1(Puzzle):
    day = 1

    def __init__(self, data=None):
        super(Day1, self).__init__(data)
        self.prep()

    def prep(self):
        """organize and sort the data"""
        self.left: List[int] = []
        self.right: List[int] = []

        for line in self.data:
            locs = line.split()
            self.left.append(int(locs[0]))
            self.right.append(int(locs[1]))
        self.left.sort()
        self.right.sort()

    def part1(self) -> int:
        diffs = map(lambda x, y: abs(x - y), self.left, self.right)
        return sum(diffs)

    def part2(self) -> int:
        right = Counter(self.right)
        return sum([x * right[x] for x in self.left])
