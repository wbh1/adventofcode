from adventofcode.utils.Puzzle import Puzzle
from typing import List
import re


class Day2(Puzzle):
    day = 2

    @staticmethod
    def is_safe(levels: List[int], problem_dampener=False) -> bool:
        safe = True
        # check if it's increasing or decreasing
        if not sorted(levels) == levels and not sorted(levels, reverse=True) == levels:
            safe = False
            if problem_dampener:
                safe = True
                # print(set(sorted(levels)))
                # print(levels)

                # sorted
                if (
                    len(
                        [
                            lvl
                            for i, lvl in enumerate(sorted(levels))
                            if lvl != levels[i]
                        ]
                    )
                    > 2
                ):
                    print("not safe sorted:", levels)
                    # reverse sorted
                    if (
                        len(
                            [
                                lvl
                                for i, lvl in enumerate(sorted(levels, reverse=True))
                                if lvl != levels[i]
                            ]
                        )
                        > 2
                    ):
                        print("not safe reverse sorted:", levels)
                        safe = False
                    else:
                        print("safe reverse sorted:", levels)
                        safe = True
                else:
                    print("safe sorted:", levels)
                    safe = True

            if not safe:
                return safe

        for i, lvl in enumerate(levels):
            if i >= len(levels) - 1:
                break
            if not 3 >= abs(lvl - levels[i + 1]) >= 1:
                if problem_dampener:
                    print(f"checking if is_safe for {levels[:i] + levels[i+1:]}")
                    if not Day2.is_safe(levels[:i] + levels[i + 1 :]):
                        return Day2.is_safe(levels[: i + 1] + levels[i + 2 :])
                    else:
                        safe = True
                else:
                    safe = False
        return safe

    def part1(self) -> int:
        # Whether or not it's safe. True if safe.
        report_statuses: List[bool] = []
        for line in self.data:
            levels = [int(x) for x in line.split()]
            report_statuses.append(self.is_safe(levels))
        return report_statuses.count(True)

    # 615 is too low
    def part2(self) -> int:
        report_statuses: List[bool] = []
        for line in self.data:
            levels = [int(x) for x in line.split()]
            report_statuses.append(self.is_safe(levels, problem_dampener=True))
            if not report_statuses[-1]:
                print(report_statuses[-1], levels)
        return report_statuses.count(True)
