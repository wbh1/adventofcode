from collections import defaultdict
from typing import Tuple

from adventofcode.utils.grid import deltas_2d
from adventofcode.utils.Puzzle import Puzzle


class Day4(Puzzle):
    day = 4

    def __init__(self, data=None):
        super().__init__(data=data)
        self.grid = defaultdict(
            lambda: "",
            {
                (y, x): self.data[y][x]
                for y in range(len(self.data))
                for x in range(len(self.data[0]))
            },
        )

    def x_mas(self):
        # To be valid, we just need to ensure that each letter A has an "M" and an "S"
        # on each diagonal
        DIAGS = [[(-1, -1), (1, 1)], [(1, -1), (-1, 1)]]
        need = ["M", "S"]
        xmas_count = 0
        for coordinate, letter in self.grid.items():
            if letter == "A":
                found = True
                for line in DIAGS:
                    adjacents = [
                        self.grid.get((coordinate[0] + d[0], coordinate[1] + d[1]), "")
                        for d in line
                    ]
                    adjacents.sort()
                    if adjacents != need:
                        found = False
                xmas_count += 1 if found else 0
        return xmas_count

    def word_search(self, coordinate: Tuple[int, int], word="MAS"):
        """
        coordinate should be a (y,x) coordinate of an "X" letter (or other starting letter)
        """
        matches = 0
        y, x = coordinate
        for direction in deltas_2d():
            letters = []
            for i in range(1, 4):
                y_delta, x_delta = direction[0] * i, direction[1] * i
                letters.append(self.grid[(y + y_delta, x + x_delta)])
            if "".join(letters) == word:
                matches += 1
        return matches

    def part1(self) -> int:
        matches = 0
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                if self.grid[(y, x)] == "X":
                    matches += self.word_search((y, x))
        return matches

    def part2(self) -> int:
        return self.x_mas()
