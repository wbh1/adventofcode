from typing import List

from adventofcode.utils.Puzzle import Puzzle


class Day2(Puzzle):
    day = 2

    @staticmethod
    def is_safe(levels: List[int]) -> bool:
        deltas = set([levels[i] - levels[i + 1] for i in range(len(levels) - 1)])
        if deltas <= {1, 2, 3} or deltas <= {-1, -2, -3}:
            return True
        return False

    def part1(self) -> int:
        # Whether or not it's safe. True if safe.
        report_statuses: List[bool] = []
        for line in self.data:
            levels = [int(x) for x in line.split()]
            report_statuses.append(self.is_safe(levels))
        return report_statuses.count(True)

    def part2(self) -> int:
        report_statuses: List[bool] = []
        for line in self.data:
            levels = [int(x) for x in line.split()]
            # Safe if one entry is removed
            report_statuses.append(
                any(
                    self.is_safe(levels[:i] + levels[i + 1 :])
                    for i in range(len(levels))
                )
            )

        return report_statuses.count(True)
