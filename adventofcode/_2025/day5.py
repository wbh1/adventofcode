from typing import List, Tuple
from adventofcode.utils.Puzzle import Puzzle


class Day5(Puzzle):
  day = 5

  def __init__(self, data=None, debug=False):
    super().__init__(data, debug)

    split = self.data.index("")
    self.ingredient_ranges = self.data[:split]
    self.ingredients = self.data[split + 1 :]

  def part1(self) -> int:
    ranges = [(int(a), int(b)) for a, b in (r.split("-", 1) for r in self.ingredient_ranges if r)]
    return sum(1 for v in map(int, self.ingredients) if any(lo <= v <= hi for lo, hi in ranges))

  def flatten_ranges(self):
    """Combine ranges to the maximum possible extent"""
    self.ingredient_ranges = sorted(self.ingredient_ranges, key=lambda x: int(x.split("-")[0]))
    merged: List[Tuple[int, int]] = []
    for r in self.ingredient_ranges:
      s, e = map(int, r.split("-"))
      if not merged or s > merged[-1][1]:
        merged.append((s, e))
      else:
        # Overlap or touch: extend the current range
        merged[-1] = (merged[-1][0], max(merged[-1][1], e))

    self.ingredient_ranges = [f"{s}-{e}" for s, e in merged]

  def part2(self) -> int:
    self.flatten_ranges()
    fresh_ids = 0
    for r in self.ingredient_ranges:
      low, high = map(int, r.split("-", 1))
      fresh_ids += high - low + 1
    return fresh_ids
