import re

from adventofcode.utils.Puzzle import Puzzle


class Day3(Puzzle):
    day = 3

    def part1(self) -> int:
        pattern = re.compile(r"mul\((?P<num1>\d{,3}),(?P<num2>\d{,3})\)")
        total = 0
        for line in self.data:
            for match in pattern.finditer(line):
                total += int(match.group("num1")) * int(match.group("num2"))
        return total

    def part2(self) -> int:
        pattern = re.compile(
            r"(?P<inst>do\(\)|don't\(\))|mul\((?P<num1>\d{,3}),(?P<num2>\d{,3})\)"
        )
        total = 0
        mul_enabled = True
        for line in self.data:
            for match in pattern.finditer(line):
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

