import os
from typing import List

from adventofcode.utils.Puzzle import Puzzle


class Day5(Puzzle):
    day = 5

    def __init__(self, data=None):
        if data is not None:
            self.data = data
        else:
            input_dir = os.getenv("AOC_INPUT_DIR", "inputs")
            with open(os.path.join(input_dir, f"day{self.day}.txt")) as f:
                # self.data = f.read().splitlines()
                self.data = f.read()
        self.rules = [
            tuple(r.split("|")) for r in self.data.split("\n\n")[0].split("\n")
        ]
        self.page_runs = [
            [p for p in page_run.split(",")]
            for page_run in self.data.split("\n\n")[1].split("\n")
            if page_run  # avoid trailing newline
        ]

    def is_valid(self, page_run: List[str]) -> bool:
        for i, p in enumerate(page_run):
            for np in page_run[i + 1 :]:
                if (np, p) in self.rules:
                    return False
        return True

    def bubble_sort(self, page_run: List[str]) -> List[str]:
        changed = True
        while changed:
            changed = False
            for i in range(len(page_run)):
                for ni in range(i + 1, len(page_run)):
                    if (page_run[ni], page_run[i]) in self.rules:
                        page_run[i], page_run[ni] = page_run[ni], page_run[i]
                        changed = True
        return page_run

    def part1(self) -> int:
        ok_runs = []
        for p in self.page_runs:
            if self.is_valid(p):
                ok_runs.append(p)
        return sum(int(r[len(r) // 2]) for r in ok_runs)

    def part2(self) -> int:
        bad_runs = []
        for p in self.page_runs:
            if not self.is_valid(p):
                bad_runs.append(p)
        for i, r in enumerate(bad_runs):
            bad_runs[i] = self.bubble_sort(r)

        return sum(int(r[len(r) // 2]) for r in bad_runs)
