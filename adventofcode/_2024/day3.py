import re

from adventofcode.utils.Puzzle import Puzzle


class Day3(Puzzle):
    day = 3
    pattern = re.compile(
        r"(?P<inst>do\(\)|don't\(\))|mul\((?P<num1>\d{,3}),(?P<num2>\d{,3})\)"
    )

    def part1(self) -> int:
        return sum(
            int(match.group("num1") or 0) * int(match.group("num2") or 0)
            for line in self.data
            for match in self.pattern.finditer(line)
        )

    def part2(self) -> int:
        total = 0
        mul_enabled = True
        for line in self.data:
            for match in self.pattern.finditer(line):
                if inst := match.group("inst"):
                    if inst == "don't()":
                        mul_enabled = False
                    elif inst == "do()":
                        mul_enabled = True
                    else:
                        raise ValueError(f"Why did {inst} match? Idk how to handle it.")
                else:
                    if mul_enabled:
                        total += int(match.group("num1")) * int(match.group("num2"))

        return total

