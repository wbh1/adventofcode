from collections import defaultdict
from typing import List, Tuple

from adventofcode._2023.day3 import DC, DR
from adventofcode.utils.Puzzle import Puzzle


class Day4(Puzzle):
    day = 4
    WORD = "XMAS"
    matches: List[List[Tuple[int, int]]] = []
    match_count = 0

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
                if found:
                    xmas_count += 1
        return xmas_count

    def adjacent_points(
        self,
        coordinate: Tuple[int, int],
        word_start=True,
        direction: Tuple[int, int] | None = None,
    ) -> bool:
        y, x = coordinate
        letter = self.grid[(y, x)]
        # Must start with X
        if word_start and letter != self.WORD[0]:
            return False
        # If we reached S, hooray
        elif letter == self.WORD[-1]:
            return True
        # What letter comes next?
        next_letter = self.WORD[self.WORD.index(letter) + 1]
        # If we're already moving in a direction, continue moving that way
        if direction is not None:
            y_delta, x_delta = direction
            if self.grid[(y + y_delta, x + x_delta)] == next_letter:
                return self.adjacent_points(
                    (y + y_delta, x + x_delta),
                    word_start=False,
                    direction=direction,
                )
            else:
                return False
        # if we're just starting out
        else:
            for y_delta, x_delta in zip(DR, DC):
                if self.grid[(y + y_delta, x + x_delta)] == next_letter:
                    if self.adjacent_points(
                        (y + y_delta, x + x_delta),
                        word_start=False,
                        direction=(y_delta, x_delta),
                    ):
                        self.match_count += 1
                    else:
                        continue
        return False

    def part1(self) -> int:
        matches = 0
        for y in range(len(self.data)):
            self.cur_line = y + 1
            starting_matches = self.match_count
            for x in range(len(self.data[y])):
                matches += 1 if self.adjacent_points((y, x)) else 0
            print(f"{self.match_count-starting_matches} new matches after line {y+1}")
        return self.match_count

    def part2(self) -> int:
        return self.x_mas()
